import flet as ft
import socket
import time
import ipaddress
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def validate_strict_ipv4(ip_str):
    if ip_str.count(".") != 3:
        return False
    try:
        ipaddress.IPv4Address(ip_str)
        return True
    except ValueError:
        return False

def scan_single_port(ip, port, stop_event, timeout=0.5):
    if stop_event.is_set():
        return None
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((ip, port)) == 0:
                return port
    except:
        pass
    return None

def main(page: ft.Page):
    page.title = "Pro Port Scanner"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0D1117"
    page.padding = 16
    page.scroll = ft.ScrollMode.AUTO

    stop_event = threading.Event()
    is_scanning = False

    # Header Banner
    header = ft.Container(
        content=ft.Column([
            ft.Text("PRO TCP PORT SCANNER", size=20, weight=ft.FontWeight.BOLD, color="#58A6FF"),
            ft.Text("Full Range (1 - 65535) | Multi-Threaded", size=12, color="#8B949E"),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=15,
        border_radius=12,
        bgcolor="#161B22",
        border=ft.border.all(1, "#30363D"),
        alignment=ft.alignment.center,
    )

    # IP Input Field
    ip_input = ft.TextField(
        label="Target IPv4 Address (e.g. 103.111.x.x)",
        hint_text="192.168.1.1",
        border_color="#58A6FF",
        focused_border_color="#3FB950",
        text_size=16,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    error_text = ft.Text("", color="#F85149", size=13, weight=ft.FontWeight.BOLD, visible=False)

    # Progress Bar & Live Stats
    progress_bar = ft.ProgressBar(value=0, color="#3FB950", bgcolor="#21262D", height=14, border_radius=7)
    status_label = ft.Text("Ready to scan", size=14, weight=ft.FontWeight.BOLD, color="#C9D1D9")
    pct_done_text = ft.Text("Done: 0.0%", size=13, color="#3FB950", weight=ft.FontWeight.BOLD)
    pct_left_text = ft.Text("Left: 100.0%", size=13, color="#F85149", weight=ft.FontWeight.BOLD)
    time_text = ft.Text("Elapsed: 00m 00s | ETA: --", size=13, color="#D29922")

    progress_card = ft.Container(
        content=ft.Column([
            status_label,
            progress_bar,
            ft.Row([pct_done_text, pct_left_text], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            time_text,
        ], spacing=8),
        padding=15,
        border_radius=12,
        bgcolor="#161B22",
        border=ft.border.all(1, "#30363D"),
        visible=False,
    )

    # Results List
    results_header = ft.Text("Open Ports Found: 0", size=15, weight=ft.FontWeight.BOLD, color="#58A6FF", visible=False)
    results_list = ft.Column(spacing=8)

    def run_scan(target_ip):
        nonlocal is_scanning
        total_ports = 65535
        completed = 0
        open_count = 0
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=250) as executor:
            futures = {executor.submit(scan_single_port, target_ip, port, stop_event): port for port in range(1, total_ports + 1)}

            for future in as_completed(futures):
                if stop_event.is_set():
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                completed += 1
                res = future.result()

                if res is not None:
                    open_count += 1
                    service = get_service_name(res)
                    results_header.value = f"Open Ports Found: {open_count}"
                    results_list.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.Text(f"✔ PORT {res}", size=15, weight=ft.FontWeight.BOLD, color="#3FB950"),
                                ft.Text(f"Service: {service}", size=14, color="#D29922"),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            padding=12,
                            border_radius=8,
                            bgcolor="#161B22",
                            border=ft.border.all(1, "#238636"),
                        )
                    )
                    page.update()

                if completed % 50 == 0 or completed == total_ports:
                    elapsed = time.time() - start_time
                    pct_done = (completed / total_ports) * 100
                    pct_left = 100.0 - pct_done

                    if completed > 0 and elapsed > 0:
                        speed = completed / elapsed
                        eta_sec = int((total_ports - completed) / speed)
                    else:
                        eta_sec = 0

                    e_min, e_sec = divmod(int(elapsed), 60)
                    eta_min, eta_sec = divmod(eta_sec, 60)

                    progress_bar.value = completed / total_ports
                    status_label.value = f"Scanning {target_ip} ({completed}/{total_ports})"
                    pct_done_text.value = f"Done: {pct_done:.1f}%"
                    pct_left_text.value = f"Left: {pct_left:.1f}%"
                    time_text.value = f"Elapsed: {e_min:02d}m {e_sec:02d}s  |  ETA: {eta_min:02d}m {eta_sec:02d}s"
                    page.update()

        is_scanning = False
        start_btn.disabled = False
        stop_btn.disabled = True
        if stop_event.is_set():
            status_label.value = "Scan Stopped by User!"
            status_label.color = "#F85149"
        else:
            status_label.value = f"Scan Completed! ({open_count} Open Ports)"
            status_label.color = "#3FB950"
        page.update()

    def on_start_click(e):
        nonlocal is_scanning
        target = ip_input.value.strip()

        if not validate_strict_ipv4(target):
            error_text.value = f"✖ Error: '{target}' is invalid! Enter full 4-part IP (e.g. 103.111.10.1)"
            error_text.visible = True
            page.update()
            return

        error_text.visible = False
        stop_event.clear()
        is_scanning = True
        start_btn.disabled = True
        stop_btn.disabled = False

        results_list.controls.clear()
        results_header.value = "Open Ports Found: 0"
        results_header.visible = True
        progress_card.visible = True
        progress_bar.value = 0
        status_label.color = "#58A6FF"
        status_label.value = f"Starting scan on {target}..."
        page.update()

        threading.Thread(target=run_scan, args=(target,), daemon=True).start()

    def on_stop_click(e):
        stop_event.set()
        stop_btn.disabled = True
        status_label.value = "Stopping scan..."
        page.update()

    start_btn = ft.ElevatedButton(
        "START SCAN",
        icon=ft.Icons.PLAY_ARROW,
        bgcolor="#238636",
        color="white",
        on_click=on_start_click,
        expand=True,
        height=45,
    )

    stop_btn = ft.ElevatedButton(
        "STOP",
        icon=ft.Icons.STOP,
        bgcolor="#DA3633",
        color="white",
        on_click=on_stop_click,
        disabled=True,
        expand=True,
        height=45,
    )

    page.add(
        header,
        ft.Container(height=5),
        ip_input,
        error_text,
        ft.Row([start_btn, stop_btn], spacing=10),
        ft.Container(height=5),
        progress_card,
        ft.Container(height=5),
        results_header,
        results_list,
    )

ft.app(target=main)
