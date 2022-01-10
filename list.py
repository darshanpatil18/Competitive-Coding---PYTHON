mylist=["HI",2,3.3]#variable declaration
print(mylist)
print(mylist[1])#indexing
print(mylist[1:3])#slicing
mylist[1]="MANGO"#updation
print(mylist)
print(len(mylist))#length of the list(number of values in the variable)
mylist.append("darshan")#adding values at the end
print(mylist)
mylist.insert(1,"HELLO")#inserting values at the specified position
print(mylist)
mylist.pop()#deleting elements from last position
print(mylist)
mylist.remove("HELLO")#deleting elements from specified position using value
print(mylist)
del mylist[0]#deleting elements from specified position using index value
print(mylist)
l=mylist.copy()#copying from one lists to another lists
print(l)
k=l#referencing from one list to another
print(k)
print(mylist + l)
print(mylist*3)
s=[1,2,3]
print(2 in s)#for checking whether elemts is present in the list
for i in s:#for retrieving value from the lists
	print(i)
m=[[1,2,3],[4,5,6]]#matrices declaration
print(m[0])#printing a row
print(m[0][2])#printing a specific value from matix	
x=[1, 2] + list("34")
print(x)
res = [c * 4 for c in 'SPAM']            
print(res)

