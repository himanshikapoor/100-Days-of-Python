with open ("Input/Names/invited_names.txt") as names_file:
    list_of_names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.readlines()
    for name in list_of_names:
        name = name.strip("\n")
        str = content[0].replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter_file:
            new_letter_file.write(str)
            for line in content[1:]:
                new_letter_file.write(line)