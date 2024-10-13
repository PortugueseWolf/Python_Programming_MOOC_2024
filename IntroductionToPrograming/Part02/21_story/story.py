words = ""
last_word = ""
count = 0
while True:
    word = input("Please type in a word: ")

    if word == "end" or word == last_word:
        print(words)
        break
    
    if count == 0:
        words += word
        count += 1
        last_word = word
        continue
        
    last_word = word
    words += " " + word
