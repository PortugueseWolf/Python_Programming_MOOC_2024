def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1

def line(n, x):
    if x == "":
        x = "*"
    print(x[0:1] * n)

if __name__ == "__main__":
    square_of_hashes(5)