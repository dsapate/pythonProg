list_1=[1,2]
list_2=[3,4]
list_3=[]
list_3.append(list_1)
list_3.append(list_2)

list_4=[5,6]
list_5=[7,8]
list_6=[]
list_6.append(list_4)
list_6.append(list_5)
print list_3
print list_6
print list_3[0][0]
print list_6[0][0]
result=0
for i,j in range(len(list_3),len(list_6)):
	for k.l in range(len(list_3),len(list_6)):
		result=list_3[i][j]+list_6[k][l]
print result
	
	
