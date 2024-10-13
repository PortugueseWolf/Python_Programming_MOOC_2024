def shape(t_height, t_car, b_heigt, b_car):
    i = 1
    while i <= t_height:
        line(i, t_car)
        i += 1
    i = 1
    while i <= b_heigt:
        line(t_height, b_car)
        i += 1

def line(n, x):
    if x == "":
        x = "*"
    print(x[0:1] * n)

if __name__ == "__main__":
    shape(2, "o", 4, "+")