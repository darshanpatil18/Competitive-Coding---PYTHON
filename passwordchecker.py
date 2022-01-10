import re
passwd=input()
if 5<len(passwd)<17:
	for i in range(len(passwd)):
		if re.match("#-@-$",passwd[i]):
			if re.match("[A-Za-z][A-Za-z]","passwd"):
				print("VALID PASSWORD")
		else:
			print("INVALID PASSWORD")
else:
	print("INVALID PASSWORD")	
