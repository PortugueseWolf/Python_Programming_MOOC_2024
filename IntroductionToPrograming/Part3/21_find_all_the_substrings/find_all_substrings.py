word = input("Please type in a word: ")
char = input("Please type in a character: ")

if char in word:
    index = word.find(char)
    while index < len(word) + 3:
        print(word[index:index + 3])
        word = word[index : index]
        index
