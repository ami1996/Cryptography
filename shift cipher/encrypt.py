plain = open('Plain_Text.txt','r')
cipher = open('Cipher_Text.txt','w')
shift = int(input("enter shift number: "))
for char in plain.read():
	if char == ' ':
		cipher.write(char)
	elif char.isupper():
		cipher.write(chr((ord(char) + shift - 65) % 26 + 65))
	else:
		cipher.write(chr((ord(char) + shift - 97) % 26 + 97))
cipher.write("\n")
cipher.close()