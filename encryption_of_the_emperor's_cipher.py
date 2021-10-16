alphabet = "abcdefghijklmnopqrstuvwxyz"
newMessage = ""

message = input("Please enter a message")
key = int(input("Enter a key (1-26)"))

status = True
while status:
    if key <= 0 or key > 26:
       print("Wrong number!!! Try it again")
       key = int(input("Enter a key (1-26)"))
    else:
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position + key) % 26
                newCharacter = alphabet[newPosition]
                #print("The new character is:", newCharacter)
                newMessage += newCharacter
            else:
                newMessage += character
        status = False

print("Your new message is", newMessage)
