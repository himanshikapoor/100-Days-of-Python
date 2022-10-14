import random
name_list = ["Alex", "Eleanor", "Beth", "Dave"]

# Generating a dictionary with marks using existing list
students_scores = {name : random.randint(1, 100) for name in name_list}
print(students_scores)

# Generating a dictionary using existing dictionary
passed_students = {name : marks for (name, marks) in students_scores.items() if marks >= 50}
print(passed_students)
