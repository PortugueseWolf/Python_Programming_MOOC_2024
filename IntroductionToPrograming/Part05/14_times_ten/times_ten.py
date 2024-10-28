def times_ten(start_index: int, end_index: int) -> dict:
    dictionary = {}
    
    while start_index <= end_index:
        dictionary[start_index] = (start_index * 10)
        start_index += 1

    return dictionary

if __name__ == "__main__":
    d = times_ten(3,6)
    print(d)