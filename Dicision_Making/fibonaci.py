def fibo(num):
	if num==1:
		return 1
	for i in range(1,num+1):
		return num+fibo(num-1)
num=input("Enter Number : ")
result=fibo(num)
print result
