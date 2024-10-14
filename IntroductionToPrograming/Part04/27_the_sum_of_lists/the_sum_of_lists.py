def list_sum(first: list, second: list) -> list:
    return_list = []
    i = 0
    while i < len(first):
        return_list.append(first[i] + second[i])
        i += 1
    return return_list

if __name__ == "__main__":

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]