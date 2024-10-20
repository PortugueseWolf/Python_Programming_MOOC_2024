def no_shouting(list: list) -> bool:
    return_list = []

    for i in list:
        if i.isupper():
            continue
        return_list.append(i)
    
    return return_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)