def all_the_longest(list: list) -> list:
    longest = ""
    return_list = []
    
    for i in list:
        if len(i) > len(longest):
            longest = i

    for i in list:
        if len(i) == len(longest):
            return_list.append(i)
    
    return return_list

if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']