x=int(input())
y=int(input())
sumx=1
sumy=1
for i in range(2,x,+1):
	if (x%i==0):
		sumx=sumx+i
for j in range(2,y,+1):
	if (y%j==0):
		sumy=sumy+j
if (sumx==y and sumy==x):
	print("YES")
else:
	print("NO")
