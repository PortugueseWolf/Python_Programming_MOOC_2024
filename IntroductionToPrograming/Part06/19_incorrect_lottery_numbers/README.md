
# Incorrect lottery numbers

The file lottery_numbers.csv containts winning lottery numbers in the following format:

```markdown
week 1;5,7,11,13,23,24,30
week 2;9,13,14,24,34,35,37
...etc...
```

Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

The week number is incorrect:

```markdown
week zzc;1,5,13,22,24,25,26
```

One or more numbers are not correct:

```markdown
week 22;1,**,5,6,13,2b,34
```

Too few numbers:

```markdown
week 13;4,6,17,19,24,33
```

The numbers are too small or large:

```markdown
week 39;5,9,15,35,39,41,105
```

The same number appears twice:

```markdown
week 41;5,12,3,35,12,14,36
```

Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.
