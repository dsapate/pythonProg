def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
n=input("Enter a Number : ")
result=fact(n)
print result
