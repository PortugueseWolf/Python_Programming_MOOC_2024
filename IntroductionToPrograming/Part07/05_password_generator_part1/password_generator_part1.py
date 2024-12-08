from random import randint

def generate_password(x: int) -> str:
    password = ""

    for i in range(x):
        password += chr(randint(97, 122))

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))