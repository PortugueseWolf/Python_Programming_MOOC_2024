from datetime import datetime

if False:
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
else:
    day = 1
    month = 1
    year = 1900

age = datetime(year, month, day)
millenium = datetime(2000,1,1)
days = (millenium - age).days

if age.year < millenium.year:
    print(f"You were {days-1} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")