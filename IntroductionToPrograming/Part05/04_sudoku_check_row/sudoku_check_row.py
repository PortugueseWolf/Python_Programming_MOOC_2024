def row_correct(sudoku: list, row_no: int) -> bool:
    i = 0

    for n in sudoku:
        if i == row_no:
                        
            if n.count(1) > 1 or n.count(2) > 1 or n.count(3) > 1 or n.count(4) > 1 or n.count(5) > 1 or n.count(6) > 1 or n.count(7) > 1 or n.count(8) > 1 or n.count(9) > 1:
                return False
            return True
        
        i += 1

if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
    [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],   # rivi 1
    [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],   # rivi 2
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # rivi 3
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
    [ 0, 0, 7, 8, 0, 3, 9, 6, 6 ],   # rivi 6
    [ 3, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
    [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],   # rivi 8
    ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
