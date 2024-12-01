
# Diary

Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.

NB: the automatic tests for this exercise will change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

The program should work as follows:

```markdown
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: Today I ate porridge
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: I went to the sauna in the evening
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!
```

When the program is executed for the second time, this should happen:

```markdown
1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!
```

**NB**: this exercise doesn't ask you to write any functions, so you should **not** place any code within an if __name__ == "__main__" block.
