from random import randint
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def Binary(message):
	alphabet = '01234567'
	newMessage = ''
	key =8
	message=int(message)
	while (message>0):
 		newPosition = message%key
 		newCharacter = alphabet[newPosition]
 		newMessage += newCharacter
 		message=message//key
	return newMessage[::-1]

def BD(message):
	newMessage=0
	t = len(message)-1
	for char in message:
  		char = int(char)
  		ans = (8**t)*char
  		ans = int(ans)
  		newMessage = newMessage+ans
  		t = t-1
	return newMessage
def generate_otp(filename):
	filename=str(filename)
	with open(filename + ".key","w") as f:
		for i in range(100):
			numg=randint(0,26)
			f.write(str(Binary(numg))+"\n")
def load_sheet(filename):
	with open(filename, "r") as f:
		contents = f.read().splitlines()
	return contents
def get_plaintext():
	plaintext = input('Please type your message: ')
	return plaintext.lower()
def load_file(filename):
	global i
	with open(filename, "r") as f:
		contents = f.read()
		for i in contents:
			print
	return contents
def save_file(filename, data):
	with open(filename, 'w') as f:
		f.write(data)
def encrypt(plaintext, sheet):
	leng=len(sheet)
	ciphertext = ''
	for position, character in enumerate(plaintext):
		if character not in ALPHABET:
			ciphertext += character
		else:
			s=sheet[position%leng]
			b=BD(s)
			encrypted = ((ALPHABET.index(character) + int(b))%26)
			ciphertext += ALPHABET[encrypted]
	return ciphertext
def decrypt(ciphertext, sheet):
	global i
	leng=len(sheet)
	plaintext = ''
	for position, character in enumerate(ciphertext):
		if character not in ALPHABET:
			plaintext += character
		else:
			s=sheet[position%leng]
			b=BD(s)
			decrypted = ((ALPHABET.index(character) - int(b))%26)
			plaintext += ALPHABET[decrypted]
	return plaintext

