from ctypes import windll
import win32gui
import win32con
import time
import json
import sys
import os

os.system("title Scheduled Shutdown - Made by Zithular")

if not os.path.exists(os.path.join(os.getenv("ProgramData"), "Scheduled Shutdown")):
    os.makedirs(os.path.join(os.getenv("ProgramData"), "Scheduled Shutdown"))

if not os.path.exists(os.path.join(os.path.join(os.getenv("ProgramData"), "Scheduled Shutdown"), "Settings.json")):
    Data = {
        "FirstTimeOpening": True,
        "GuideShown": False,
        "DateFormat": None,
    }

    with open(os.path.join(os.path.join(os.getenv("ProgramData"), "Scheduled Shutdown"), "Settings.json"), "w") as file:
        json.dump(Data, file)

with open(os.path.join(os.path.join(os.getenv("ProgramData"), "Scheduled Shutdown"), "Settings.json"), "r") as file:
    Data = json.load(file)

    if Data["FirstTimeOpening"] == True:
        for char in "Welcome to Scheduled Shutdown!":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print("\n")

    if not Data.get("DateFormat", ""):
        print("Please choose your preferred date format:")
        print("[1] MM/DD/YYYY")
        print("[2] DD/MM/YYYY")
        DateFormatting = input("> ")

        if DateFormatting == "1" or DateFormatting == "[1]" or DateFormatting == "MM/DD/YYYY":
            Data["DateFormat"] = "MM/DD/YYYY"
        elif DateFormatting == "2" or DateFormatting == "[2]" or DateFormatting == "DD/MM/YYYY":
            Data["DateFormat"] = "DD/MM/YYYY"
        else:
            print("Invalid choice.")

        print()

    if Data["FirstTimeOpening"] and not Data["GuideShown"]:
        print("Would you like to see the guide before starting?")
        Guide = input("> ")
        print()

        if Guide == 'yes' or Guide == 'y':
            Data["GuideShown"] = True
            print("Welcome to Scheduled Shutdown!")
            print("This program allows you to schedule a shutdown time for your computer.")
            print("You can specify the date and time.")
            print()

        elif Guide == 'no' or Guide == 'n':
            Data["GuideShown"] = False

    with open(os.path.join(os.path.join(os.getenv("ProgramData"), "Scheduled Shutdown"), "Settings.json"), "w") as file:
        json.dump(Data, file)

Data["FirstTimeOpening"] = False

print("Please enter the date you would like to schedule the shutdown:")
ShutdownDate = input("> ")
print()

print("What time would you like to shutdown?")
ShutdownTime = input("> ")
print()

try:
    Hour, Minute, Second = time.strptime(ShutdownTime, "%I:%M:%S %p").tm_hour, time.strptime(ShutdownTime, "%I:%M:%S %p").tm_min, time.strptime(ShutdownTime, "%I:%M:%S %p").tm_sec
    if Data["DateFormat"] == "MM/DD/YYYY":
        Month, Day, Year = map(int, ShutdownDate.split("/"))
    elif Data["DateFormat"] == "DD/MM/YYYY":
        Day, Month, Year = map(int, ShutdownDate.split("/"))
except ValueError:
    print("Invalid date or time format.")
    time.sleep(3)
    exit()

for _ in range(int(3 / (2 * 0.5))):
    os.system("cls")
    print("Thank you!", end="", flush=True)
    time.sleep(0.5)
    os.system("cls")

win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

while time.mktime(time.localtime()) < time.mktime((Year, Month, Day, Hour, Minute, Second, -1, -1, -1)):
    time.sleep(1)

os.system("shutdown /s /f /t 0")
