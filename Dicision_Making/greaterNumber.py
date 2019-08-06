for i in range(3):
	number=input("Enter a Number : ")
print number
for i in range(4):
	if(number[i+1]>number[i]):
		store=number[i+1]
	else:
		store=number[i]
		print store
