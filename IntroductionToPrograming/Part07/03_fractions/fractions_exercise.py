from fractions import Fraction

def fractionate(amount: int) -> list:
    to_return = []
    for i in range(0, amount):
        to_return.append(Fraction(1, amount))

    return to_return

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))