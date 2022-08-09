from prettytable import PrettyTable

# declaring an object
table = PrettyTable()

# calling methods
table.add_column("Pokemon_name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# using attributes
table.align = "l"
print(table)
