
# Find all the substrings

Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

```markdown
Please type in a word: mammoth
Please type in a character: m
mam
mmo
mot
```

```markdown
Please type in a word: banana
Please type in a character: n
nan
```

**Hint** the following example may give you some inspiration as to how this exercise could be tackled:

```python
word = input("Word: ")
while True:
    if len(word) == 0:
        break
    print(word)
    word = word[2:]
```

```markdown
Word: mammoth
mammoth
mmoth
oth
h
```
