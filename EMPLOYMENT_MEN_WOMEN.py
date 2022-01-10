sex=input()
age=int(input())
if sex=="W" and age<=40:
	print("WOMEN CAN WORK IN OFFICES WITH AGE=",age)
elif sex=="M" and 40<=age<=60:
	print("MEN CAN WORK IN OFFICES WITH AGE=",age)
elif sex=="M" and age>=60:
	print("WOMEN CAN WORK ANYWHERE WITH AGE=",age)
else:
		print("NO OPTION")

