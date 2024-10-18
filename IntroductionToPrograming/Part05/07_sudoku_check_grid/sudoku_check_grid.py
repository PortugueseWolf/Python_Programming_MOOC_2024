def sudoku_grid_correct(sudoku: list) -> bool:

    if not row_correct(sudoku) or not column_correct(sudoku):
        return False
    
    grids = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for i in grids:
        if not block_correct(sudoku,i[0],i[1]):
            return False

    return True

def row_correct(sudoku: list) -> bool:

    for n in sudoku:               
        if n.count(1) > 1 or n.count(2) > 1 or n.count(3) > 1 or n.count(4) > 1 or n.count(5) > 1 or n.count(6) > 1 or n.count(7) > 1 or n.count(8) > 1 or n.count(9) > 1:
            return False
        
    return True


def column_correct(sudoku: list) -> bool:
    column_index = 0

    while column_index < 9:
        column = []
        for i in sudoku:
            column.append(i[column_index])

        if column.count(1) > 1 or column.count(2) > 1 or column.count(3) > 1 or column.count(4) > 1 or column.count(5) > 1 or column.count(6) > 1 or column.count(7) > 1 or column.count(8) > 1 or column.count(9) > 1:
            return False
        column_index += 1
    
    return True

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
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
    [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
    [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
    [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
    [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
    [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
    [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
    [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
    [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    ]
    print(sudoku_grid_correct(sudoku3))