# 🔍 Pro TCP Port Scanner (Android APK)

A fast, multi-threaded **TCP Port Scanner** built with **Python** and **Flet (Flutter)** for Android. Scan the full port range (`1 - 65535`) of any IPv4 address with real-time progress tracking, live percentage stats, ETA calculation, and built-in **Deep Port Inspection**.

অ্যান্ড্রয়েডের জন্য **Python** এবং **Flet (Flutter)** দিয়ে তৈরি একটি দ্রুতগতির মাল্টি-থ্রেডেড **TCP Port Scanner** অ্যাপ। এর মাধ্যমে যেকোনো IPv4 অ্যাড্রেসের সম্পূর্ণ পোর্ট রেঞ্জ (`1 - 65535`) স্ক্যান করার পাশাপাশি লাইভ প্রোগ্রেস বার, পার্সেন্টেজ, আনুমানিক সময় (ETA) এবং **Deep Port Inspection** সুবিধা পাওয়া যায়।

---

## ✨ Key Features | মূল ফিচারসমূহ

- **Full-Range Multi-Threaded Scanning:** Scans all **65,535 TCP ports** rapidly using 250 concurrent worker threads.
  *(২৫০টি ওয়ার্কার থ্রেড ব্যবহার করে খুব দ্রুত সবগুলো **৬৫,৫৩৫টি TCP পোর্ট** স্ক্যান করে।)*
- **Strict IPv4 Validation:** Automatically detects and blocks incomplete or malformed IP addresses before starting a scan.
  *(স্ক্যান শুরুর আগেই অসম্পূর্ণ বা ভুল IP অ্যাড্রেস শনাক্ত করে সতর্কবার্তা দেখায়।)*
- **Live Progress Dashboard:** Real-time progress bar with **Done %**, **Left %**, **Elapsed Time**, and dynamic **ETA**.
  *(রিয়েল-টাইম লোডিং বারের সাথে কত শতাংশ হয়েছে, কত বাকি আছে, অতিবাহিত সময় এবং আর কতক্ষণ লাগবে তা লাইভ দেখায়।)*
- **Deep Port Inspector (Tap-to-Scan):** Tap any discovered open port card to probe its **Raw TCP Banner**, **HTTP/HTTPS Status**, **Server Header**, and **HTML Page Title**.
  *(খুঁজে পাওয়া যেকোনো ওপেন পোর্টের কার্ডে ট্যাপ করলে ওই পোর্টের ভেতরের সার্ভার ইনফো, ব্যানার ও পেজ টাইটেল চেক করা যায়।)*
- **Quick Actions:** One-tap **Open in Browser** (`http://` / `https://`) and **Copy `IP:Port`** directly from the inspection popup.
  *(পপ-আপ থেকেই এক ক্লিকে ব্রাউজারে ওপেন এবং `IP:Port` কপি করার সুবিধা।)*
- **Automated Cloud APK Build:** Configured with **GitHub Actions** to automatically compile the Android `.apk` on every push.
  *(**GitHub Actions**-এর মাধ্যমে কোড আপডেট করলেই অটোমেটিক ক্লাউডে নতুন `.apk` ফাইল তৈরি হয়।)*

---

## 📥 How to Download & Install | ডাউনলোড ও ইনস্টল করার নিয়ম

1. Go to the **[Actions](../../actions)** tab at the top of this repository. *(রিপোজিটরির ওপরে থাকা **Actions** ট্যাবে যান।)*
2. Click on the latest completed workflow run with a green checkmark (`✔`). *(সবুজ টিক চিহ্ন `✔` যুক্ত সর্বশেষ বিল্ডটিতে ক্লিক করুন।)*
3. Scroll down to the **Artifacts** section and download **`Pro-Port-Scanner-APK`**. *(নিচে **Artifacts** সেকশন থেকে **`Pro-Port-Scanner-APK`** ডাউনলোড করুন।)*
4. Extract the `.zip` file on your Android device and install **`app-release.apk`**. *(ফোনে `.zip` ফাইলটি Extract করে ভেতরের **`app-release.apk`** ইনস্টল করুন।)*

---

## 🛠️ Tech Stack | ব্যবহৃত প্রযুক্তি

- **Language:** Python 3.11
- **UI Framework:** Flet (`0.28.3`) / Flutter
- **Networking:** Python `socket`, `ssl`, `ipaddress`, `concurrent.futures`
- **CI/CD:** GitHub Actions

---

## ⚠️ Disclaimer | সতর্কবার্তা

This tool is intended strictly for **network administration, authorized security auditing, and educational purposes**. Always ensure you have explicit permission before scanning external networks or IP addresses.

*(এই অ্যাপটি শুধুমাত্র নেটওয়ার্ক অ্যাডমিনিস্ট্রেশন, অনুমোদিত সিকিউরিটি টেস্টিং এবং শিক্ষামূলক কাজে ব্যবহারের জন্য তৈরি। অনুমতি ছাড়া অন্য কারো নেটওয়ার্ক বা আইপি স্ক্যান করা থেকে বিরত থাকুন।)*
