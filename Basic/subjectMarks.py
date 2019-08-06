subject=[]
sum=0
for i in range(5):
	sub=input("Enter Marks of Subjects : ")
	subject.append(sub)
	sum=sum+subject[i]
print subject
print sum/5
