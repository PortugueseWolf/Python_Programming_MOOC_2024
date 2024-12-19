import json

def print_persons(filename: str) -> None:

    with open(filename) as my_file:
        data = my_file.read()

    hobbies = json.loads(data)

    for hobbie in hobbies:
        if len(hobbie["hobbies"]) == 0:
            print(f"{hobbie["name"]} {hobbie["age"]} years ()")
        else:
            print(f"{hobbie["name"]} {hobbie["age"]} years (", end="")
            for i in range(len(hobbie["hobbies"])):
                if i < len(hobbie["hobbies"]) - 1:
                    print(hobbie["hobbies"][i] + ",", end=" ")
                else:
                    print(hobbie["hobbies"][i] + ")")                

if __name__ == "__main__":
    print_persons("file1.json")