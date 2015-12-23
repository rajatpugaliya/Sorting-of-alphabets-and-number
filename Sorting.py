# program for sorting in number and alphabets
print "1. Alphabets 2. Number"
a=input("enter the choice")
if a==1:
	list=["a","e","s","r","a"]
	print "1. Ascending 2. Descending"		
	a1=input("enter the choice")
	if a1==1:	
		list.sort() # used to sort the list
		print list
	elif a1==2:
		list.sort() 
		list.reverse() # used to reverse the list
		print list
	else:
		print "wrong input choice"
elif a==2:
	list=[1,5,2,6,4,3]
	print "1. Ascending 2. Descending"		
	a1=input("enter the choice")
	if a1==1:	
		list.sort()
		print list
	elif a1==2:
		list.sort()
		list.reverse()
		print list
	else:
		print "wrong input choice"

else:
	print "wrong input choice"