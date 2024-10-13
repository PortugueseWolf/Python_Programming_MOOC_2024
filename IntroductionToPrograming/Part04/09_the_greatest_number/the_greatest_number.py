def greatest_number(a, b, c):
    if a >= b:
        if a >= c:
            return a
        if c >= b:
            return c
        
    if b >= a:
        if b >= c:
            return b
        if c >= a:
            return c
        
if __name__ == "__main__":
    print(greatest_number(3, 4, 1))
        