
# define new variable with name x and value 2.0
x= 2.0
print(x)
print(type(x))

#convert this variable to int
conInt = int(x)
print(conInt)

# increase the x value by 6 using assignment operator


def addfun(x=0,y=0):
    print(x+y)

addfun(2+4)

# 	- get the module of the new x by 3


#write s simple ternary operator
name = "sarah"
print("yesnametrur") if name =="sara" else print("not nametrue")

list= [2,4,6,8,10]

# - check to see if 4 in this list or not
if 4 in list:
    print("yes this 4")
else:
    print("not equle 4")


# - check to see if 4 and 6 in this list on not
if all([4 ,6]) in list:
    print("yes this 4,6")
else:
    print("not equle 4 ,6")

# - check to see if 3 or 6 in this list

if all([6,3]) in list:
    print("yes this 3,6")
else:
    print("not equle 3 ,6")

# - check to see if 2 , 4 and 5 in this list
if all([2,4,5]) in list:
    print("yes this 2,4,5")
else:
    print("not equle 2,4,5")

