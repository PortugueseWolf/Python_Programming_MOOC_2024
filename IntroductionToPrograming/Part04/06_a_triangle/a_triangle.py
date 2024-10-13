def triangle(n):
    i = 1
    while i <= n:
        line(i, "#")
        i += 1


def line(n, x):
    if x == "":
        x = "*"
    print(x[0:1] * n)

if __name__ == "__main__":
    triangle(5)