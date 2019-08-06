count1=0
count2=0
string_1="Mutex Programming"
string_2="Mutex"
for i in range(len(string_1)):
	count1+=1
for i in range(len(string_2)):
	count2+=1
if(count1>count2):
	print string_1
else:
	print string_2
