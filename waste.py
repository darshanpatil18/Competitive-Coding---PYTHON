n=int(input())
sum=0
l=[]
su=[]
sumi=0
sumj=0
sumk=0
for i in range(1,n+1):
    sum=sum+i
for i in range(0,sum):
    y=int(input())
    l.append(y)
for i in range(0,sum-5):
    sumi=0
    sumi=sumi+l[i]
    for j in range(1,sum-3):
        sumj=0
        sumj=sumj+l[j]+sumi
        for k in range(3,sum):
            sumk=sumj+l[k]
            su.append(sumk)
            sumk=0
su.sort()
print(su[sum-1])
