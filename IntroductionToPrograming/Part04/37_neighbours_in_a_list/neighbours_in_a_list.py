def longest_series_of_neighbours(list: list) -> int:
    count = 0
    last = list[0]
    biggest = 0
    for i in list:
        if i - 1 == last or i + 1 == last:
            if count == 0:
                count += 2
            else:
                count += 1
            last = i
            if count > biggest:
                biggest = count
            continue
        count = 0
        last = i
    
    return biggest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))