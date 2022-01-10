n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
for i in range(len(l)-1,0,-1):
	for j in range(i):
		if l[j]>l[j+1]:
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp
		else:
			l[j]=l[j]
print(l)
