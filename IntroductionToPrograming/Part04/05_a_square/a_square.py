def square(n, x):
    i = 0
    
    while i < n:
        line(n, x)
        i += 1

def line(n, x):
    if x == "":
        x = "*"
    print(x[0:1] * n)

if __name__ == "__main__":
    square(5, "X")