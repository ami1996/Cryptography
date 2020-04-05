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
	cipher.write('key #' + str(key) + ' : ' + trans)
cipher.close()
