
# Course grading part 4

Let's revisit the course grading project from the previous section.

As we left if last time, the program read and processed files containing student information, completed exercises and exam results. We'll add a file containing information about the course. An example of the format of the file:

```markdown
name: Introduction to Programming
study credits: 5
```

The program should then create two files. There should be a file called results.txt with the following contents:

```markdown
Introduction to Programming, 5 credits
======================================
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
```

The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.

Additionally, there should be a file called results.csv with the following format:

```markdown
12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3
```

When the program is executed, it should look like this:

```markdown
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
Course information: course1.txt
Results written to files results.txt and results.csv
```

That is, the program only asks for the names of the input files. All output should be written to the files. The user will only see a message confirming this.

**NB**: this exercise doesn't ask you to write any functions, so you should **not** place any code within an if __name__ == "__main__" block.
