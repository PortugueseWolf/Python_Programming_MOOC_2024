dictionary = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        word = line.replace("\n", "")
        dictionary.append(word)

if True:
    user_input = input("Write text: ")
else:
    user_input = "a aah aahing aaahii ab"

words = user_input.split(" ")
for word in words:
    if word.lower() not in dictionary:
        print(f"*{word}*", end=" ")
        continue
    print(word, end=" ")
