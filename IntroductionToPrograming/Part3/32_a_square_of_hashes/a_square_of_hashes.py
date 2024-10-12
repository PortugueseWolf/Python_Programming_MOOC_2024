def hash_square(length):
    n = 1
    while n <= length:
        print("#" * length)
        n += 1

if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)
