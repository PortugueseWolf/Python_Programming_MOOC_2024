times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical lunch? "))
groceries = float(input("How much money fo you spend on groceries in a week? "))
daily = (times * price + groceries) / 7
weekly = times * price + groceries
print(f"Average food ependiture:\nDaily: {daily} euros\nWeekly: {weekly} euros")