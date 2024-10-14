def distinct_numbers(list: list) -> list:
    to_return = []
    
    for n in sorted(list):
        if n in to_return:
            list.remove(n)
            continue
        to_return.append(n)
    
    return to_return

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]