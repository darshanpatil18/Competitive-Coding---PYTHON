pan=input()
if len(pan)==10:
	for i in range(0,5):
		if pan[i].isalpha()==False:
			print("Invalid pan")
			break
	for j in range(5,9):
		if pan[i].isnumeric()==False:
			print("Invalid pan")
			break
	if pan[9].isalpha==True:
		print("Invalid pan")
else:
	print("Invalid pan")
