n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
for i in range(0,len(l)-1):
	min=i
	for j in range(i+1,n):
		if l[j]<l[min]:
			min=j
	temp=l[i]
	l[i]=l[min]
	l[min]=temp
print(l)
