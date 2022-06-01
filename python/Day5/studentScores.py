student_scores = input("Input a list of student scores ").split()

print(student_scores)

maximum = 0

for i in student_scores:
    if i > maximum:
        maximum = i

print(f"The heighest score in the class is: {maximum}")
