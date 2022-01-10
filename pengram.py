s=input()
s1=s.replace(" ","")
sum=0
print(s1)
for i in range(0,len(s1)):
	x=s1[i]
	for j in range(i+1,len(s1)):
		if(s1[j]==x):
			sum=sum+1
if(sum>0):
	print("Not pengram")
else:
	print("Pengram")
