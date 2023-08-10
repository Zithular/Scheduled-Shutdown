# Scheduled-Shutdown
Scheduled Shutdown is a Python application that allows you to schedule a shutdown time for your computer. You can specify the date and time for the shutdown, and the app will automatically perform the shutdown at the specified time.

## Downloading
Please either press the green Code Button, then press extract as zip or if you have Git installed, open command prompt and change to your chosen directory and type `git clone https://github.com/Zithular/Scheduled-Shutdown/`.

## Prerequisites
Run the `Install.bat` file. If it fails, please try to read the error code and find out the issue. It is likely that your python or pip is outdated. Please update these. Additionally, make sure you are on a Windows Operating System that has Python installed.

## Usage
Open a terminal or command prompt, and navigate to the directory where you cloned/downloaded the Scheduled Shutdown app. Run the following command to start the application: `python ScheduledShutdown.py`. The application will greet you with a welcome message and ask for your preferred date format. Choose one of the following formats:
```
[1] MM/DD/YYYY
[2] DD/MM/YYYY
```
If it is your first time opening the app, you will be asked if you want to see the guide before starting. You can choose "yes" or "no" accordingly. Then, enter the date you would like to schedule the shutdown in the format based on your choice above and enter the time you would like to schedule the shutdown in the format "HH:MM:SS AM/PM". The app will then wait until it is or has been the Scheduled shutdown time, and shutdown the computer.

## Configuration
The application stores its settings in a JSON file called `Settings.json`, located in `ProgramData`. You can manually edit this file to modify the application's behavior if needed.

## Disclaimer
Use this program at your own risk. The author and contributors are not responsible for any data loss or damage caused by using this application.
