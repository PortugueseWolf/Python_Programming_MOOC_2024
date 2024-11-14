def largest() -> int:
    largest_number = 0

    with open("numbers.txt") as new_file:
        for line in new_file:
            if int(line) > largest_number:
                largest_number = int(line)
    
    return largest_number

if __name__ == "__main__":  
    print(largest())