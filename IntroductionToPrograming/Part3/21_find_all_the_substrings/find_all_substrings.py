word = input("Please type in a word: ")
char = input("Please type in a character: ")

if char in word:
    while True:
        index = word.find(char)
        #print(index)
        if index >= len(word) - 2 or index < 0:
            break
        print(word[index:index + 3])
        word = word[index + 1:]