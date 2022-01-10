st=input()
sum=0
for i in range(0,len(st)-1,1):
	if st[i]+st[i+1]=='da':
		sum=sum+1
	continue
print(sum)
