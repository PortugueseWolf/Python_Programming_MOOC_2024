def palindromes(word: str) -> bool:
    if word == word[::-1]:
        return True
    return False

while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break
    print("that wasn't a palindrome")