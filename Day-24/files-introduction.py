# Method 1
file = open("myfile.txt")
contents = file.read()
print(contents)
file.close()

# Method 2 (No need to call the close function)
with open("myfile.txt", mode="w") as file:
    file.write("\nThis is inside Day-24 folder")