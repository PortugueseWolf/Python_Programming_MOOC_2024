
# Fix the code: Print a single line

Each print command usually prints out a line of its own, complete with a change of line at the end. However, if the print command is given an additional argument end = "", it will not print a line change.

For example:

```python
print("Hi ", end="")
print("there!")
```

Sample output

```markdown
Hi there!
```

Please fix this program so that the entire calculation, complete with result, is printed out on a single line. Do not change the number of print commands used.

```python
print(5)
print(" + ")
print(8)
print(" - ")
print(4)
print(" = ")
print(5 + 8 - 4)
```
