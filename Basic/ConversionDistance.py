
print("1.Kilometer to mile \n 2. celsius to Fahrenheit")
choice=input("Enter your choice : ")
while(choice>=0):
	
	if(choice==1):
		kilo=input("Enetr Kilometers : ")
		mile=kilo*0.6213
		print("Mile Distance is "+str(mile))
		break
	elif(choice==2):
		celsius=input("Enetr Celsisus : ")
		frahe=(0*9/5)+32
		print("Fahrenheit Distance is "+str(frahe))
		break
	else:
			print("Your choice is wrong")
