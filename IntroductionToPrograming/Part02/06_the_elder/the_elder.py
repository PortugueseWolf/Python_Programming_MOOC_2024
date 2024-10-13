print("Person 1:")
first_name = input("Name: ")
first_age = int(input("Age: "))

print("Person 2:")
second_name = input("Name: ")
second_age = int(input("Age: "))

if first_age > second_age:
    print(f"The elder is {first_name}")
elif second_age > first_age:
    print(f"The elder is {second_name}")
else:
    print(f"{first_name} and {second_name} are the same age")