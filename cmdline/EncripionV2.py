
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i = 0
newMessage = ''
keys=[3,1,4,1,5]
message=input("Enter A Message:")

for character in message:
 i=i+1
 i=i % 4
 if character in alphabet:
  position = alphabet.find(character)
  newPosition = (position + keys[i]) % 26
  newCharacter = alphabet[newPosition]
  newMessage += newCharacter
 else:
  newMessage += character
print("Your Message is ",newMessage)
