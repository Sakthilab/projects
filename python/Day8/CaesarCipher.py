from art import logo


def caesar(c, t, s):
    final = ""
    if c == "decode":
            s *= -1
    for i in t:
        if i in alphabet:
            position = alphabet.index(i)        
            new_position = position + s
            final += alphabet[new_position]
        else:
            final += i

    print(f"Here's the {choice}d result: {final}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

flag = True

while flag:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    shift = shift % 26
    caesar(c=choice, t=text, s=shift)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == "no":
        flag = False
        print("Goodbye")
