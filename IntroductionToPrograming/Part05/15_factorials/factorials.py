import math

def factorials(n: int) -> dict:
    dictionary = {}
    
    for element in range(1, n + 1):
        dictionary[element] = (math.factorial(element))

    return dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])