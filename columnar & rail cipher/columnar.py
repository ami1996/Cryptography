file = open('message.txt','r')
message = file.read()
print("\nThe message is:",message)

def encryption(message):
	key = list(map(int,input("\nenter the key: ").split()))

	for c in range(-(len(message)%len(key))%len(key)):
		message += 'x'

	A = [[] for i in range(len(key))]
	for i in range(len(message)):
		A[i%len(key)].append(message[i])

	d = {}
	for i in range(len(key)):
		d[key[i]] = A[i]

	file = open('message.txt','w')
	for i in range(len(key)):
		for j in d[i]:
			file.write(j)

def decryption(message):
	key = list(map(int,input("\nenter the key: ").split()))

	A = [[] for i in range(len(key))]
	for i in range(len(key)):
		A[i] = message[key[i]*(len(message)//4):(key[i]+1)*(len(message)//4)]
	A = ''.join(A)

	file = open('message.txt','w')
	for i in range(len(message)//len(key)):
		for j in range(i,len(message),len(message)//len(key)):
			file.write(A[j])

print("\n1.encryption\n2.decryption")
i = int(input("\nenter your choice: "))
if(i == 1):
	encryption(message);
elif(i==2):
	decryption(message);
else:
	print("wrong choice")
