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

def add_number(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    sudoku[row_no][column_no] = number



if __name__ == "__main__":
    sudoku  = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)