def encrypt():
	plain = open('Plain_Text.txt','r')
	cipher = open('Cipher_Text.txt','w')
	shift = int(input("enter shift number: "))
	for char in plain.read():
		if (char == ' ' or char == '.' or char == ','):
			cipher.write(char)
		elif char.isupper():
			cipher.write(chr((ord(char) + shift - 65) % 26 + 65))
		else:
			cipher.write(chr((ord(char) + shift - 97) % 26 + 97))
	cipher.close()
	return ""

def decrypt():
	plain = open('Plain_Text.txt','w')
	cipher = open('Cipher_Text.txt','r')
	shift = int(input("enter shift number: "))
	for char in cipher.read():
		if(char == ' ' or char == '.' or char == ','):
			plain.write(char)
		elif char.isupper():
			plain.write(chr((ord(char) - shift - 65) % 26 + 65))
		else:
			plain.write(chr((ord(char) - shift - 97) % 26 + 97))
	plain.close()
	return ""

def bruteforce():
	cipher = open('Cipher_Text.txt','r+')
	message = ''
	for i in cipher.read():
		message += i
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

	for key in range(len(LETTERS)):
		trans = ''
		for symbol in message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol)
				num = num - key
				if num < 0:
					num = num + len(LETTERS)
				trans = trans + LETTERS[num]
			else:
				trans = trans + symbol
		cipher.write('key #'+str(key)+' : '+trans +"\n")
	cipher.close()
	return ""

def frequency_analysis():
	cipher = open('Cipher_Text.txt','r+')
	message = ''
	for i in cipher.read():
		message += i

	ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def getItemAtIndexZero(x):
		return x[0]

	letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
	for letter in message.upper():
		if letter in LETTERS:
			letterCount[letter] += 1
	freqToLetter = {}
	for letter in LETTERS:
		if letterCount[letter] not in freqToLetter:
			freqToLetter[letterCount[letter]] = [letter]
		else:
			freqToLetter[letterCount[letter]].append(letter)

	for freq in freqToLetter:
		freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
		freqToLetter[freq] = ''.join(freqToLetter[freq])
	freqPairs = list(freqToLetter.items())
	freqPairs.sort(key=getItemAtIndexZero, reverse=True)
	freqOrder = []
	for freqPair in freqPairs:
		freqOrder.append(freqPair[1])
	freqOrder = ''.join(freqOrder)

	for j in range(26):
		key = ord(freqOrder[0]) - ord(ETAOIN[j])
		l = [str(x) for x in message]
		for i in range(len(l)-1):
			if(l[i] == " "):
				pass
			elif (l[i].isupper()):
				l[i] = chr((ord(l[i]) - key -65)%26+65)
			else:
				l[i] = chr((ord(l[i]) - key -97)%26+97)
		trans = ''.join(l)
		cipher.write('key #'+str(j)+' : '+trans+"\n")
	cipher.close()
	return ""

def numbers_to_strings(arg):
	switcher = { 
	    0: encrypt,
	    1: decrypt, 
	    2: bruteforce,
	    3: frequency_analysis,
	}
	fun = switcher.get(arg, lambda: "Invalid")
	return fun()

print("0: encrypt")
print("1: decrypt")
print("2: bruteforce")
print("3: frequency_analysis")
print(numbers_to_strings(int(input("!!!!!! Instructions : Don't try to decrypt any decrypted message. !!!!!!\n Enter your choice : "))))
