number=int(input())
unitdigit=number%10
hundreddigits=(number%100)//10
thousand=number//100
arm=unitdigit**3+hundreddigits**3+thousand**3
print("NUMBER IS ARMSTRONG") if arm==number else print("NUMBER IS NOT ARMSTRONG")


