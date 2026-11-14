# 🔍 Pro TCP Port Scanner (Android APK)

A fast, multi-threaded **TCP Port Scanner** built with **Python** and **Flet (Flutter)** for Android. Scan the full port range (`1 - 65535`) of any IPv4 address with real-time progress tracking, live percentage stats, ETA calculation, and built-in **Deep Port Inspection**.

---

## ✨ Key Features

- **Full-Range Multi-Threaded Scanning:** Scans all **65,535 TCP ports** rapidly using 250 concurrent worker threads.
- **Strict IPv4 Validation:** Automatically detects and blocks incomplete or malformed IP addresses before starting a scan.
- **Live Progress Dashboard:**
  - Real-time solid progress bar
  - **Done %** and **Left %** live counters
  - **Elapsed Time** and dynamic **ETA** (Estimated Time Remaining)
- **Deep Port Inspector (Tap-to-Scan):** Tap any discovered open port card to probe its **Raw TCP Banner**, **HTTP/HTTPS Status**, **Server Header**, and **HTML Page Title**.
- **Quick Actions:** One-tap **Open in Browser** (`http://` / `https://`) and **Copy `IP:Port`** directly from the inspection popup.
- **Automated Cloud APK Build:** Configured with **GitHub Actions** to automatically compile the Android `.apk` on every push.

---

## 📥 How to Download & Install the APK

1. Go to the **[Actions](../../actions)** tab at the top of this repository.
2. Click on the latest completed workflow run with a green checkmark (`✔`).
3. Scroll down to the **Artifacts** section and download **`Pro-Port-Scanner-APK`**.
4. Extract the `.zip` file on your Android device and install **`app-release.apk`**.
   *(If Google Play Protect shows a warning for an unrecognized developer, tap **More details → Install anyway**.)*

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **UI Framework:** Flet (`0.28.3`) / Flutter
- **Networking:** Python `socket`, `ssl`, `ipaddress`, `concurrent.futures`
- **CI/CD:** GitHub Actions

---

## ⚠️ Disclaimer

This tool is intended strictly for **network administration, authorized security auditing, and educational purposes**. Always ensure you have explicit permission before scanning external networks or IP addresses.
