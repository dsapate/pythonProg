def dict(count):
	d={}
	sum=0
	sum1=0
	for i in range(1,count+1):
		d[i]=i*2
		sum1*=d[i]
		sum*=i
	print("key addtion of dictionary "+str(sum))
	print("value addition of dictionary is "+str(sum1))
print("Enter count")
count=input()
dict(count)
