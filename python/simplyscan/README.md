
<pre class="overflow-visible! px-0!" data-start="214" data-end="926"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span># 🔍 SimplyScan</span><br/><br/><span>> A lightweight multithreaded port scanner built with Python for fast and efficient network reconnaissance.</span><br/><br/><span>---</span><br/><br/><span>## 📸 Overview</span><br/><br/><span>SimplyScan is a Python-based port scanner designed to identify open ports and commonly associated services on a target system.  </span><br/><span>This project was built to reinforce core cybersecurity concepts including networking, socket programming, and multithreading.</span><br/><br/><span>---</span><br/><br/><span>## ⚙️ Features</span><br/><br/><span>- ⚡ Fast multi-threaded scanning  </span><br/><span>- 🔎 Scans ports 1–1024 (common ports)  </span><br/><span>- 🧠 Service detection (FTP, SSH, HTTP, etc.)  </span><br/><span>- 💻 Simple and clean CLI interface  </span><br/><span>- 🛠️ Beginner-friendly and extensible  </span><br/><br/><span>---</span><br/><br/><span>## 🚀 Usage</span><br/><br/><span>### Run the scanner:</span><br/><span>```bash</span><br/><span>python3 simplyscan.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### Example:

<pre class="overflow-visible! px-0!" data-start="941" data-end="1074"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Enter Target IP Address: 192.168.1.1</span><br/><br/><span>Scanning Target IP 192.168.1.1...</span><br/><br/><span>[+] Port 22 (SSH) is OPEN</span><br/><span>[+] Port 80 (HTTP) is OPEN</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🧪 Technologies Used

* Python 3
* `socket` (network connections)
* `threading` (parallel execution)
* CLI-based interaction

---

## 🧠 Key Concepts Learned

* TCP/IP and port communication
* Multithreading for performance optimization
* Writing clean and readable CLI tools
* Mapping ports to services

---

## 📁 Project Structure

<pre class="overflow-visible! px-0!" data-start="1435" data-end="1486"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>simplyscan/</span><br/><span>├── simplyscan.py</span><br/><span>└── README.md</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## ⚠️ Disclaimer

This tool is intended for  **educational purposes only** .

Only scan systems you own or have explicit permission to test.

---

## 🚧 Future Improvements

* Add command-line arguments (`-t`, `-p`, etc.)
* Expand port range customization
* Improve output formatting (color, tables)
* Add logging functionality
* Implement banner grabbing

---

## 👤 Author

**Ryan McClure**

* GitHub: [https://github.com/PhishingForCompliments]()

---

## ⭐ Final Note

This project marks the beginning of my journey into cybersecurity tooling and offensive security concepts.

More advanced tools and lab environments will be added as I continue to build and learn.
