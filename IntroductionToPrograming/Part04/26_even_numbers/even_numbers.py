def even_numbers(list: list) -> list:
    return_list = []

    for n in list:
        if n % 2 == 0:
            return_list.append(n)
    
    return return_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)