def spruce(size):
    print("a spruce!")
    
    i = 1
    star = 1
    space = size - i
    
    while i <= size:
        print(" " * space + "*" * star)
        i += 1
        star += 2
        space -= 1
    
    print(" " * (size - 1) + "*" * 1)

if __name__ == "__main__":
    spruce(3)
    spruce(5)
