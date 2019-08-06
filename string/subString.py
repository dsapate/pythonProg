count=0
string_1="Mutex programming"
string_2="Mutex"
l=len(string_2)
for i in range(len(string_1)):
	for j in range(len(string_2)):
		if(string_1[i]==string_2[j]):
			count+=1
if(l==count):
	print("String present in main string")
else:
	print("check condition")
