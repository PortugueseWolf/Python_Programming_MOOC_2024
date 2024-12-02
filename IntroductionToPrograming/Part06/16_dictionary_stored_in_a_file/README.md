
# Dictionary stored in a file

Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.

The program should work as follows:

```markdown
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: auto
The word in English: car
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: roska
The word in English: garbage
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: laukku
The word in English: bag
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: bag
roska - garbage
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: car
auto - car
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: laukku
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 3
Bye!
```

The dictionary entries should be written to a file called dictionary.txt. The program should first read the contents of the file. New entries are written to the end of the file whenever they are added to the dictionary.

The format of the data stored in the dictionary is up to you.

**NB**: the automatic tests for this exercise may change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

**NB2**: this exercise doesn't ask you to write any functions, so you should **not** place any code within an if \_\_name\_\_ == "\_\_main\_\_" block.
