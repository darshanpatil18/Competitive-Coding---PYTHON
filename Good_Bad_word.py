w=input()
ll=[]
for i in range(len(w)):
    x=ord(w[i])
    ll.append(x)
s=set(ll)
if len(s)<len(w):
    print("Bad")
else:
	print("Good")
