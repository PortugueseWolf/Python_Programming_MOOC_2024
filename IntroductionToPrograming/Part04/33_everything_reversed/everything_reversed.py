def everything_reversed(list: list) -> list:
    return_list = []

    for i in list[::-1]:
        return_list.append(f"{i[::-1]}")

    return return_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)