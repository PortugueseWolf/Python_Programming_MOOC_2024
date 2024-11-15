def matrix_to_list() -> list:
    list = []

    with open("matrix.txt") as new_file:
        for line in new_file:
            numbers = line.replace("\n", "")
            number_split = numbers.split(",")
            list_numbers = []
            
            for number in number_split:
                list_numbers.append(int(number))
            
            list.append(list_numbers)
    
    return list

def matrix_sum() -> int:
    sum = 0
    
    for each in row_sums():
        sum += each
    
    return sum

def matrix_max() -> int:
    maximum = 0

    for each in matrix_to_list():
        if max(each) > maximum:
            maximum = max(each)
    
    return maximum

def row_sums() -> list:
    sum_per_row = []

    for line in matrix_to_list():
        sum = 0

        for number in line:
            sum += int(number)
        sum_per_row.append(sum)
    
    return sum_per_row

if __name__ == "__main__":
    print(row_sums())
    print(matrix_max())
    print(matrix_sum())