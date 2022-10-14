import pandas

# Iterating a dictionary
students_marks = {
    "student" : ["A", "B", "C"],
    "marks" : [10, 20, 30]
}

for (name, score) in students_marks.items():
    print(name)
    print(score)

# Creating a pandas data frame
students_data_frame = pandas.DataFrame(students_marks)
print(students_data_frame)

# Iterating a data frame (using for loop)
for (key, value) in students_data_frame.items():
    print(value)

# Iterating using iterrows (looping through rows) 
for (index, row) in students_data_frame.iterrows():
    print(row)

# Getting hold of column
for(index, row) in students_data_frame.iterrows():
    print(row.marks)

# Getting hold of a particular row
for (index, row) in students_data_frame.iterrows():
    if row.student == "A":
        print(row.marks)