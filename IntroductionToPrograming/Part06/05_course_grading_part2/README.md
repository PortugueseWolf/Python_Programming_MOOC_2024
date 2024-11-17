
# Course grading part 2

Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file. The contents of the file follow this format:

```markdown
id;e1;e2;e3
12345678;4;1;4
12345687;3;5;3
12345699;10;2;2
```

In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.

```markdown
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
pekka peloton 0
jaana javanainen 1
liisa virtanen 3
```

Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.

The final grade for the course is determined based on the sum of exam and exercise points according to the following table:

|exam points + exercise points| grade |
|---|---|
|0-140 | (fail) |
|15-17 | 1 |
|18-20 | 2 |
|21-23 | 3 |
|24-27 | 4 |
|28- | 5 |

**NB**: this exercise doesn't ask you to write any functions, so you should **not** place any code within an if __name__ == "__main__" block.
