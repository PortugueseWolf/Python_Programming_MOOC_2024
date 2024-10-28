def print_sudoku(sudoku: list) -> None:
    column_counter = 0
    row_counter = 0

    for row in sudoku:
        for number in row:    

            if column_counter == 8:
                if number == 0:
                    print("_")
                else:
                    print(number)
                column_counter = 0
                continue
            
            if number == 0:
                print("_ ", end="")
            else:
                print(number, "", end="")
            
            if column_counter == 2 or column_counter == 5:
                print(" ", end="")
            
            column_counter += 1
        
        if row_counter == 2 or row_counter == 5:
                print()
        row_counter += 1

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    new_list = []
    
    for i in sudoku:
        new_list.append(i[:])

    new_list[row_no][column_no] = number
    return new_list

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)