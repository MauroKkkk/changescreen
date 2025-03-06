# Taskbar Application Switcher

This Python script leverages **pyautogui** and **OpenCV** to automate switching between AnyDesk and Chrome on the Windows taskbar. It detects the application icons via template matching and simulates mouse clicks at set intervals to alternate between the two applications.

## Features

- **Icon Detection:** Uses OpenCV to locate the AnyDesk and Chrome icons on the taskbar.
- **Automated Interaction:** Simulates mouse clicks with pyautogui to switch between applications.
- **Configurable Timing:** Allows you to set the interval between switches.
- **Basic Error Handling:** Manages cases where icons are not detected.

## Prerequisites

- Python 3.x
- [pyautogui](https://pyautogui.readthedocs.io/)
- [OpenCV](https://opencv.org/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MauroKkkk/changescreen.git
   cd changescreen
   ```

2. **Install the Required Packages:**

   ```bash
   pip install pyautogui opencv-python
   ```

## Setup

1. **Templates:**
   - Place the template images for the AnyDesk and Chrome icons in a folder named `img` within the project directory.
   - Ensure the template images are clear and cropped to only show the icon for accurate detection.

2. **Configuration:**
   - Adjust the time interval for switching by modifying the `time.sleep()` value in the script.
   - Fine-tune the template matching thresholds if necessary, to improve detection accuracy based on your screen settings.

## Usage

Run the script using Python:

```bash
python changescreen.py
```

The script will continuously capture screenshots of the Windows taskbar, detect the positions of the AnyDesk and Chrome icons, and automatically click on them at the defined intervals, effectively switching between the applications.

## Disclaimer

Automating mouse interactions and screen capturing may interfere with your regular workflow. Please use this script with caution and test it in a controlled environment before using it in a production scenario.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or open issues if you have suggestions or encounter any problems!
