print("What is the weather forecast tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
twenty = "Wear jeans and a T-shirt"
ten = "I recommend a jumper as well"
over_five = "Take a jacket with you"
bellow_five = "Make it a warm coat, actually\nI think gloves are in order"

if temperature > 20:
    print(twenty)

if temperature > 10:
    if temperature <= 20:
        print(f"{twenty}\n{ten}")

if temperature > 5:
    if temperature <= 10:
        print(f"{twenty}\n{ten}\n{over_five}")

if temperature <= 5:
    print(f"{twenty}\n{ten}\n{over_five}\n{bellow_five}")

if rain == "yes":
    print("Don't forget your umbrella!")
