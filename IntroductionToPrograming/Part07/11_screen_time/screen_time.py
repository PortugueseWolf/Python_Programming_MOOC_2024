from datetime import datetime, timedelta

if True:
    file_name = input("Filename: ")
    start_date = input("Starting date: ")
    days = int(input("Days: "))
else:
    file_name = "late_june.txt"
    start_date = "24.6.2020"
    days = 5

date = datetime.strptime(start_date, "%d.%m.%Y")

time_period = f"{date.strftime("%d.%m.%Y")}-{(date + timedelta(days=5)).strftime("%d.%m.%Y")}"

print("Please type in screen time in minutes on each day (TV computer mobile): ")

data = {}

for i in range(days):
    print_date = date + timedelta(days=i)
    hours = input(f"Screen time {print_date.strftime("%d.%m.%Y")}: ")
    splitter = hours.split(" ")       
    data[print_date] = [splitter]

total_minutes = 0

for i in data.items():
    total_minutes += int(i[1][0][0])
    total_minutes += int(i[1][0][1])
    total_minutes += int(i[1][0][2])

try:
    with open(file_name, "w") as new_file:
        new_file.write(f"Time period: {date.strftime("%d.%m.%Y")}-{(date + timedelta(days=days - 1)).strftime("%d.%m.%Y")}\n")
        new_file.write(f"Total minutes: {total_minutes}\n")
        new_file.write(f"Average minutes: {total_minutes / days}\n")

        for i in data.items():
            new_file.write(f"{i[0].strftime("%d.%m.%Y")}: {i[1][0][0]}/{i[1][0][1]}/{i[1][0][2]}\n")

except:
    print(f"Couldn't write to {file_name}.")

print(f"Data stored in file {file_name}")
