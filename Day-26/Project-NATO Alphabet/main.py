import pandas

data_df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter : row.code for (index, row) in data_df.iterrows()}

word = input("Enter a word: ").upper()
nato_code = [data_dict[letter] for letter in word if letter in data_dict]

print(nato_code)