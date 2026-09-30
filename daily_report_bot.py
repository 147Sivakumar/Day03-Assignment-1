import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip


# ============================================================
# DAILY REPORT BOT
# Gen AI Architect Program - Assignment 1
# Windows version
# ============================================================

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

# Public website
WEBSITE_URL = "https://www.google.com/search?q=weather"

# Save output files in the same folder as this Python file
OUTPUT_DIR = Path(__file__).resolve().parent

# PyAutoGUI safety:
# Move mouse to the TOP-LEFT corner to stop the program.
pyautogui.FAILSAFE = True

# Small pause between PyAutoGUI actions
pyautogui.PAUSE = 0.3


# ------------------------------------------------------------
# HELPER
# ------------------------------------------------------------

def wait(seconds):
    """Wait for the computer/application."""
    time.sleep(seconds)


# ------------------------------------------------------------
# OPEN CHROME
# ------------------------------------------------------------

def open_chrome():
    print("1. Opening Google Chrome...")

    # Windows Run dialog
    pyautogui.hotkey("win", "r")
    wait(1)

    pyautogui.write("chrome", interval=0.05)
    pyautogui.press("enter")

    # Wait for Chrome
    wait(5)

    print("   Chrome opened.")


# ------------------------------------------------------------
# GET DATA FROM WEBSITE
# ------------------------------------------------------------

def fetch_weather_data():
    print("2. Opening weather website...")

    # Go to the website
    pyautogui.hotkey("ctrl", "l")
    pyautogui.write(WEBSITE_URL, interval=0.02)
    pyautogui.press("enter")

    # Wait for webpage to load
    wait(6)

    print("   Weather page loaded.")

    # Select page text
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

    wait(1)

    # Get copied text
    page_text = pyperclip.paste()

    if not page_text.strip():
        raise RuntimeError("Could not copy information from the website.")

    # Look for a line containing temperature
    lines = [
        line.strip()
        for line in page_text.splitlines()
        if line.strip()
    ]

    temperature = None

    for line in lines:
        if "°" in line:
            temperature = line
            break

    # If temperature was not detected, use the first
    # useful piece of copied information.
    if not temperature:
        if lines:
            temperature = lines[0][:100]
        else:
            temperature = "Weather information unavailable"

    print("   Data found:", temperature)

    return temperature


# ------------------------------------------------------------
# OPEN MICROSOFT EXCEL
# ------------------------------------------------------------

def open_excel():
    print("3. Opening Microsoft Excel...")

    # Windows Run dialog
    pyautogui.hotkey("win", "r")
    wait(1)

    pyautogui.write("excel", interval=0.05)
    pyautogui.press("enter")

    # Give Excel time to open
    wait(8)

    print("   Excel opened.")


# ------------------------------------------------------------
# CREATE REPORT
# ------------------------------------------------------------

def create_report(timestamp, weather_data):
    print("4. Creating report in Excel...")

    # Try to close any start-screen selection/dialog
    pyautogui.press("esc")
    wait(1)

    # Click the first worksheet cell.
    #
    # If your Excel layout is different, this is the main
    # coordinate you may need to adjust.
    pyautogui.click(150, 180)

    wait(1)

    # --------------------------------------------------------
    # HEADER ROW
    # --------------------------------------------------------

    pyautogui.write("Date & Time")
    pyautogui.press("tab")

    pyautogui.write("Fetched Data")
    pyautogui.press("tab")

    pyautogui.write("Comment")
    pyautogui.press("enter")

    # --------------------------------------------------------
    # DATA ROW
    # --------------------------------------------------------

    pyautogui.write(timestamp)
    pyautogui.press("tab")

    # Use clipboard because weather data can contain
    # special characters such as the degree symbol.
    pyperclip.copy(weather_data)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")

    # Our comment
    pyautogui.write("Good for outdoor activities")

    wait(2)

    print("   Report row created.")


# ------------------------------------------------------------
# SAVE EXCEL FILE
# ------------------------------------------------------------

def save_excel(filename):
    print("5. Saving Excel file...")

    # Open Save As
    pyautogui.hotkey("ctrl", "shift", "s")

    wait(3)

    # Full output path
    full_path = OUTPUT_DIR / filename

    # Enter filename/path
    pyautogui.hotkey("ctrl", "a")

    pyperclip.copy(str(full_path))
    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("enter")

    wait(4)

    # If Excel asks about file format,
    # press Enter to accept the default.
    pyautogui.press("enter")

    wait(3)

    print("   Excel file saved:")
    print("  ", full_path)


# ------------------------------------------------------------
# TAKE SCREENSHOT
# ------------------------------------------------------------

def take_screenshot(filename):
    print("6. Taking screenshot of final Excel sheet...")

    screenshot_path = OUTPUT_DIR / filename

    # Capture entire screen
    screenshot = pyautogui.screenshot()

    # Save screenshot
    screenshot.save(screenshot_path)

    print("   Screenshot saved:")
    print("  ", screenshot_path)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    print()
    print("=" * 60)
    print("       DAILY REPORT AUTOMATION BOT")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # Generate current date/time automatically
    # --------------------------------------------------------

    now = datetime.now()

    # Date + time displayed in Excel
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Date used in filenames
    current_date = now.strftime("%Y-%m-%d")

    # Required Excel filename
    excel_filename = f"daily_report_{current_date}.xlsx"

    # Screenshot filename
    screenshot_filename = f"daily_report_{current_date}.png"

    print("Date & Time:", timestamp)
    print()

    try:

        # ----------------------------------------------------
        # STEP 1 - Open Chrome
        # ----------------------------------------------------

        open_chrome()

        # ----------------------------------------------------
        # STEP 2 - Fetch information
        # ----------------------------------------------------

        weather_data = fetch_weather_data()

        # ----------------------------------------------------
        # STEP 3 - Open Excel
        # ----------------------------------------------------

        open_excel()

        # ----------------------------------------------------
        # STEP 4 - Create Excel report
        # ----------------------------------------------------

        create_report(
            timestamp,
            weather_data
        )

        # ----------------------------------------------------
        # STEP 5 - Save Excel
        # ----------------------------------------------------

        save_excel(excel_filename)

        # ----------------------------------------------------
        # STEP 6 - Screenshot
        # ----------------------------------------------------

        take_screenshot(screenshot_filename)

        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        print()
        print("=" * 60)
        print("          AUTOMATION COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print()
        print("Excel file:")
        print(OUTPUT_DIR / excel_filename)
        print()
        print("Screenshot:")
        print(OUTPUT_DIR / screenshot_filename)
        print()
        print("You can now submit these files.")
        print()

    except Exception as error:

        print()
        print("=" * 60)
        print("             AUTOMATION FAILED")
        print("=" * 60)
        print()
        print("Error:")
        print(error)
        print()
        print("Check the screen and try again.")
        print()


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
