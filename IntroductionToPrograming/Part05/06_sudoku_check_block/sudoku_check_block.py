def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    row = 0
    column = column_no
    data = []
    for i in sudoku:
        if row >= row_no and row <= row_no + 2:
            while column >= column_no and column <= column_no + 2:
                data.append(i[column])
                column += 1
        column = column_no
        row += 1 

    if data.count(1) > 1 or data.count(2) > 1 or data.count(3) > 1 or data.count(4) > 1 or data.count(5) > 1 or data.count(6) > 1 or data.count(7) > 1 or data.count(8) > 1 or data.count(9) > 1:
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))