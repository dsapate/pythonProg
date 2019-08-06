f0=0
f1=1
l=[]
l.append(f0)
l.append(f1)
num=input("Enter Number : ")
print "value of f0 and f1 is "+str(f0),str(f1)
for i in range(num):
	res=f0+f1
	l.append(res)
	f0=f1
	f1=res
print("fibonacci series is => "+str(l))

