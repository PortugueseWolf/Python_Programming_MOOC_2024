def store_personal_data(person: tuple) -> None:
    with open("people.csv", "a") as data:
        data.write(f"{str(person[0])};{int(person[1])};{float(person[2])}\n")