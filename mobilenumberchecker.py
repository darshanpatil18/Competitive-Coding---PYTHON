mob=input()
if len(mob)==10 and mob[0]!=0:
	for i in range(len(mob)):
		if mob[i].isalpha()==True:
			print("Invalid number")
			break
	print("Valid number")	
else:
	print("Invalid number")	
