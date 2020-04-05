plain = open('Plain_Text.txt','w')
cipher = open('Cipher_Text.txt','r')
shift = int(input("enter shift number: "))
for char in cipher.read():
	if char == ' ':
		plain.write(char)
	elif char.isupper():
		plain.write(chr((ord(char) - shift - 65) % 26 + 65))
	else:
		plain.write(chr((ord(char) - shift - 97) % 26 + 97))
plain.close()