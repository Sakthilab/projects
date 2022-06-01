student_heights =input("Input a list of student heights ").split()

print(student_heights)

total_height = 0

for height in student_heights:
    total_height = total_height + height

print(total_height)

no_of_students = 0

for student in student_heights:
    no_of_students = no_of_students + 1

print(f"Total number of students: {no_of_students}")

average = int(total_height / no_of_students)
print(f"Average Height is: {average}")



