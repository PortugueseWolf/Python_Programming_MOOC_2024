from datetime import datetime, str
if False:
    file_name = input("Filename: ")
    start_date = input("Starting date: ")
    days = int(input("Days: "))
else:
    file_name = "late_june.txt"
    start_date = "24.6.2020"
    days = 5

date = datetime.strptime(start_date, "%d.%m.%y")

print("Please type in screen time in minutes on each day (TV computer mobile): ")
