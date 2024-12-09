from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime(year, month, day)
print(date - datetime(2000, 1, 1))