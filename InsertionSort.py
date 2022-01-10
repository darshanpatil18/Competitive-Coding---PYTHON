n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
for i in range(0,n-1):
    for j in range (0,i+1):
        if(l[i+1]<l[j]):
            temp=l[i+1]
            l[i+1]=l[j]
            l[j]=temp   
print(l)
