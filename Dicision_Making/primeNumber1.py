num=input("Enter a Number : ")
if num>1:
	for i in range(2,num):
		if(num%i==0):
			print(str(num)+" is Not a prime Number")
			break
	else:
		print(str(num)+" is a Prime Number")
