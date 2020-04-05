file = open('message.txt','r')
message = file.read()
print("\nThe message is:",message)

def encryption(text):
	rails = int(input("number of rails: "))
	m = (rails - 1) * 2
	out = ''
	for i in range(rails):
		if i % (rails - 1) == 0:
			# outer rail
			out += text[i::m]
		else:
			#inner rails
			char_pairs = zip(text[i::m], list(text[m-i::m]) + [''])
			out += ''.join(map(''.join, char_pairs))
	file = open('message.txt','w')
	file.write(out)

def decryption(t):
	r = int(input("number of rails: "))

	c = ''.join(t[dict((b,a)for a,b in enumerate(i+j for k in range(r)for i in range(r-1,len(t)+r,2*r-2)for j in[k-r+1,r+~k][:1+(r-1>k>0)]if i+j<len(t)))[m]]for m in range(len(t)))
	print(c)

print("\n1.encryption\n2.decryption")
i = int(input("\nenter your choice: "))
if(i == 1):
	encryption(message);
elif(i==2):
	decryption(message);
else:
	print("wrong choice")
