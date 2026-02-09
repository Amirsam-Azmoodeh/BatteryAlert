Markdown# BatteryAlert

A simple cross-platform Python script that monitors your laptop or desktop battery level  
and alerts you with desktop notifications + sound when the battery gets too low or too high.

## Features
- Works on **Windows**, **macOS**, and **Linux**
- Two modes:
  - **Manual mode** — you set custom low/high percentages, check interval, and alert cooldown
  - **Auto mode** — default thresholds: 10% low, 90% high, checks every ~8 seconds
- Desktop notifications using the `plyer` library
- Sound alerts:
  - Multi-tone beeps on Windows
  - System sound (`paplay` + fallback beep) on Linux
  - Spoken alert (`say`) on macOS
- Clean terminal interface with menu, emojis, screen clearing, and real-time battery info
- Smart Ctrl+C handling:
  - Inside monitoring → returns to main menu
  - Inside menu → exits the program completely

## Requirements
- Python 3.8 or higher
- Libraries:
  - `psutil` — for battery information
  - `plyer` — for desktop notifications

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/BatteryAlert.git
   cd BatteryAlert

Install dependencies:Bashpip install -r requirements.txt
Run the script:Bashpython main.py

Menu Options

1 → Manual mode (set your own thresholds and intervals)
2 → Auto mode (recommended – 10–90% range)
3 or Ctrl+C → Exit the program

While the battery is being monitored:
Ctrl+C → Return to the main menu
Notes / Limitations

Linux sound: Depends on paplay (PulseAudio/PipeWire) and the freedesktop sound theme. Falls back to terminal bell (\a) if not available.
Notifications: Require a graphical desktop environment (won't work in SSH/headless sessions).
Execution: Runs in the foreground (terminal). It is not a background/daemon service.
Tested on Windows 10/11, macOS Ventura+, Ubuntu 22.04/24.04+, Fedora, etc.

License
MIT License
Feel free to use, modify, and share!
Built with ❤️ in Python
text### Quick reminders before you push:
- Replace `YOUR_USERNAME` with your actual GitHub username (you can edit it later on GitHub if you forget now)
- Make sure the file is named exactly **`README.md`** (not REDAME.MD or anything else)
- After pushing, visit your repo page — GitHub should automatically render this README nicely at the top

If you want to add screenshots later (e.g. menu view or notification popup), you can upload images to the repo and link them in the README with Markdown like:

```markdown
![Menu screenshot](screenshots/menu.png)
Let me know when you’ve pushed it — I’d be happy to check the live repo or suggest next steps (like adding topics/tags, creating a release, etc.) 😊