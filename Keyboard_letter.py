w=input()
v=w.upper()
sumx=0 
sumy=0
sumz=0
for i in range(len(w)):
    if v[i] in "QWERTYUIOP":
        sumx=sumx+1
    elif v[i] in "ASDFGHJKL":
        sumy=sumy+1
    else:
        sumz=sumz+1
if (sumx==len(w)):
    print("Yes")
elif (sumy==len(w)):
    print("Yes")
elif(sumz==len(w)):
    print("Yes")
else:
    print("No")
