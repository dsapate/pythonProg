list_1=[3,4,6,89,22]
number=input("Enter Divisible Number : ")
for i in range(len(list_1)):
	if(list_1[i]%number!=0):
		print('')
	else:
		print list_1[i]
