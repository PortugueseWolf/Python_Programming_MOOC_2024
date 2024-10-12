def squared(word, square):
    i = 0
    to_print = word * square
    
    while i < square:
        print(to_print[0: square])
        to_print = to_print[square:]
        if len(to_print) < square:
            to_print += word * square
        i += 1

if __name__ == "__main__":
    squared("python", 15)