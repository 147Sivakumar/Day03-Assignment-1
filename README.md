Daily Report Bot – PyAutoGUI Automation
📌 Project Overview

This project is a desktop automation bot built using Python and PyAutoGUI as part of the Gen AI Architect Program – Assignment 3.

The bot automates the process of preparing a daily status report by controlling the browser and Microsoft Excel through mouse and keyboard actions, similar to how a person would operate the applications.

🎯 Objective

The goal of this project is to automate the following daily reporting workflow:

Open Google Chrome.

Navigate to a public website.

Fetch an important piece of information from the webpage.

Open Microsoft Excel.

Create a new row containing:

Current date and time

Fetched information

A short comment

Save the Excel file using the current date in the filename.

Take a screenshot of the completed Excel sheet.

🛠️ Technologies Used

Python 3

PyAutoGUI – for mouse and keyboard automation

Microsoft Excel – for creating and saving the report

Google Chrome – for accessing the public website

Pyperclip – for clipboard operations [remove if you did not use it]

OpenPyXL – for Excel file handling [remove if you did not use it]

💻 Platform

Operating System: Windows

Spreadsheet Application: Microsoft Excel

Browser: Google Chrome

📂 Project Structure
daily-report-bot/
│
├── daily_report_bot.py
├── daily_report_YYYY-MM-DD.xlsx
├── daily_report_YYYY-MM-DD.png
└── README.md

⚙️ Setup
1. Clone the repository
git clone [YOUR_GITHUB_REPOSITORY_URL]
cd daily-report-bot

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

For Windows PowerShell:

venv\Scripts\Activate.ps1


For Windows Command Prompt:

venv\Scripts\activate.bat

4. Install dependencies
pip install pyautogui


If additional libraries are used in the project:

pip install pyperclip openpyxl

▶️ Running the Bot

Run the following command:

python daily_report_bot.py


Once started, the bot automatically controls the mouse and keyboard to complete the reporting workflow.

⚠️ Important: Do not move the mouse or type on the keyboard while the bot is running because PyAutoGUI is controlling the computer.

📊 Expected Output

After a successful execution, the bot creates an Excel report containing:

Date & Time	Fetched Data	Comment
Automatically generated	Information fetched from website	Short automated comment

The Excel file is saved using the current date:

daily_report_YYYY-MM-DD.xlsx


A screenshot of the final Excel sheet is also saved:

daily_report_YYYY-MM-DD.png

📸 Sample Output
Excel Report

Add your screenshot here after uploading it to the repository:

![Daily Report Screenshot](daily_report_YYYY-MM-DD.png)

🔄 Automation Workflow
Start
  ↓
Open Chrome
  ↓
Open Public Website
  ↓
Fetch Required Information
  ↓
Open Microsoft Excel
  ↓
Enter Date & Time
  ↓
Enter Fetched Data
  ↓
Enter Comment
  ↓
Save Excel File
  ↓
Take Screenshot
  ↓
End

✨ Key Features

Automates browser interaction using PyAutoGUI

Automatically generates the current date and time

Fetches information from a public website

Creates a daily Excel report

Automatically generates a date-based filename

Saves a screenshot of the final report

Uses real mouse and keyboard automation

📁 Assignment Deliverables

This repository contains the main project files required for the assignment:

daily_report_bot.py – automation source code

Excel output file – generated daily report

Screenshot – final Excel sheet

README.md – project documentation

👨‍💻 Author

[K.Sivakumar]

Gen AI Architect Program
Assignment 3 – PyAutoGUI Automation
