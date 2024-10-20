def formatted(list: list) -> list:
    return_list = []

    for i in list:
        return_list.append(f"{i:.2f}")
    
    return return_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)