def chessboard(size):
    n = "1"
    length = 1
    height = 1
    line = ""

    while height <= size:
        while length <= size:
            line += n

            if n == "1":
                n = "0"
            else:
                n = "1"

            length += 1

        print(line)

        if size % 2 == 0:
            if n == "1":
                n = "0"
            else:
                n = "1"
        
        length = 1
        height += 1
        line = ""

if __name__ == "__main__":
    chessboard(4)
    print()
    chessboard(5)
