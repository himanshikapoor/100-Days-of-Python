# Adding 1 to list of numbers and storing it in another list
# Trivial method
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    new_n = n + 1
    new_numbers.append(new_n)

# Using list comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

# Double the numbers in a range: O/P-> [2, 4, 6, 8]
new_list = [2 * n for n in range(1, 5)]
print(new_list)

# Add names only if length of names < 5 (Using conditional list comprehension)
name_list = ["Alex", "Eleanor", "Beth", "Dave"]
new_name_list = [name.upper() for name in name_list if len(name) < 5]
print(new_name_list)
