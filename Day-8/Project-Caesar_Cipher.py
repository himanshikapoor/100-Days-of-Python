import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    str = ""
    for position in range(len(text)):
        if text[position] not in alphabet:
            str += text[position]
        elif direction == "encode":
            index = alphabet.index(text[position]) + shift
            str += alphabet[index % 26]
        elif direction == "decode": 
            index = alphabet.index(text[position]) - shift
            str += alphabet[index % 26]
    print(f"Here's the {direction}d result: {str}")

choice = "yes"
while choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    choice = input("Do you wish to continue?(yes/no)\n")
    if choice == "no":
        print("GoodBye")
