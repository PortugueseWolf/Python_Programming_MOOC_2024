def  column_correct(sudoku: list, column_no: int) -> bool:
    column = []
    
    for i in sudoku:
        column.append(i[column_no])

    if column.count(1) > 1 or column.count(2) > 1 or column.count(3) > 1 or column.count(4) > 1 or column.count(5) > 1 or column.count(6) > 1 or column.count(7) > 1 or column.count(8) > 1 or column.count(9) > 1:
        return False
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))