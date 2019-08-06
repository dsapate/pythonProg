def dict(count):
	d={}
	sum=0
	for i in range(1,count+1):
		d[i]=i*2
		sum+=i
		
print("key addtion of dictionary "+str(sum))
print("Enter count")
count=input()
dict(count)
