sum=0
number=input("Enter Number : ")
org=number
while(number>0):
	remainder=number%10
	a=remainder**3
	sum=sum+a
	number=int(number/10)
if(org==sum):
	print str(sum)+" is Armstrong Number"
else:
	print str(sum)+" is Not a Armstrong Number"

	
