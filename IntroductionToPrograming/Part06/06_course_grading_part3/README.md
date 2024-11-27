
# Course grading part 3

This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.

```markdown
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv

name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
```

Each row contains the information for a single student. The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

You might find the f-strings covered in part 4 useful here.

F-strings differentiate between strings and numbers when it comes to justifying columns:

```python
word = "python"
print(f"{word:10}continues")
print(f"{word:>10}continues")
```

```markdown
python    continues
    pythoncontinues
```

As you can see above, by default strings are justified to the left edge of the area specified for them. The > symbol can be used to justify to the right edge.

With number values the logic is reversed:

```python
number = 42
print(f"{number:10}continues")
print(f"{number:<10}continues")
```

```markdown
        42continues
42        continues
```

With numbers the default behaviour is to justify to the right edge. The symbol < can be used to justify to the left edge.

**NB**: this exercise doesn't ask you to write any functions, so you should **not** place any code within an if __name__ == "__main__" block.
