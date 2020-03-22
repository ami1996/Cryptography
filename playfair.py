import numpy as np

my_matrix = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
arr = np.array(my_matrix)

LETTER = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

message = open('message.txt','r')
m = message.read()
message.close()
text =[]
for char in m:
	if (char == "j" or char == "J"):
		text.append("I")
	elif (char != " "):
		text.append(char.upper())

key = input("enter the key : ").upper()
x = 0; repeat = 0
while(x-repeat < 25):
    if x<len(key):
        if(key[x] not in arr):
            arr[(x-repeat)//5][(x-repeat)%5] = key[x]
        else:
            repeat += 1
    else:
        if(LETTER[x-len(key)] not in arr):
            arr[(x-repeat)//5][(x-repeat)%5] = LETTER[x-len(key)]
        else:
            repeat += 1
    x += 1
print(arr)

def encrypt(text):
	for i in range(0,len(text),2):
		if(text[i] == text[i+1]):
			text.insert(i+1,"X")

	if(len(text)%2 != 0):
	    text.append("X")

	for i in range(0,len(text),2):
	    x1 = np.where(arr == text[i])
	    x2 = np.where(arr == text[i+1])
	    if(x1[1][0] == x2[1][0]): #column check
	        text[i] = arr[(x1[0][0] + 1)%5,x1[1][0]]
	        text[i+1] = arr[(x2[0][0] + 1)%5,x2[1][0]]
	    elif(x1[0][0] == x2[0][0]): #row check
	        text[i] = arr[x1[0][0],(x1[1][0] + 1)%5]
	        text[i+1] = arr[x2[0][0],(x2[1][0] + 1)%5]
	    else:
	        text[i] = arr[x1[0][0],x2[1][0]]
	        text[i+1] = arr[x2[0][0],x1[1][0]]

	return (text)

def decrypt(text):
	for i in range(0,len(text),2):
	    x1 = np.where(arr == text[i])
	    x2 = np.where(arr == text[i+1])
	    if(x1[1][0] == x2[1][0]):
	        text[i] = arr[(x1[0][0] - 1)%5,x1[1][0]]
	        text[i+1] = arr[(x2[0][0] - 1)%5,x2[1][0]]
	    elif(x1[0][0] == x2[0][0]):
	        text[i] = arr[x1[0][0],(x1[1][0] - 1)%5]
	        text[i+1] = arr[x2[0][0],(x2[1][0] - 1)%5]
	    else:
	        text[i] = arr[x1[0][0],x2[1][0]]
	        text[i+1] = arr[x2[0][0],x1[1][0]]
	
	while(len(text) != len(m)):
		if(text[-1] == "X"):
			text = text[:len(text)-1]
		elif("X" in text):
			i = text.index("X")
			if(text[i-1] == text[i+1]):
				text = text[:i]+text[i+1:]
		else:
			break 

	return (text)

def switch(arg):
	if arg > 2 :
		print("\nchoose 1 or 2...")
		return ""
	else:
		switcher = {
			1: encrypt,
			2: decrypt,
		}
		fun = switcher.get(arg)
		return fun(text)

print("\n 1: encryption \n 2: decryption")
text = switch(int(input("\nenter your choice: ")))
for i in range(len(m)):
	if(m[i] != " "):
		pass
	else:
		text.insert(i," ")
message = open("message.txt","w")
message.write(''.join(text))
message.close()