def box_of_hashes(height):
    i = 0
    while i < height:
        line(10, "#")
        i += 1


def line(n, x):
    if x == "":
        x = "*"
    print(x[0:1] * n)

if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(3)
