def transpose(matrix: list) -> None:
    new_list = []

    for row in matrix:
        new_list.append(row[:])

    for row in range(len(new_list[:])):
        for element in range(len(new_list[row])):
            matrix[element][row] = new_list[row][element]

if __name__ == "__main__":
    list = [[1,2,3],[4,5,6],[7,8,9]]
    print("original: ", list)

    transpose(list)
    print("Second original: ", list)