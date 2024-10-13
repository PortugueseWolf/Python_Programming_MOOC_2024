students = int(input("How many students on the course? "))
group = int(input("Desired group size? "))
made = students // group
if made<(students / group):
    made += 1
print(f"Number of groups formed: {made}")