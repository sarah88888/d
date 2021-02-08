
# define new variable with name x and value 2.0
x= 2.0
print(x)
print(type(x))

#convert this variable to int
conInt = int(x)
print(conInt)

# increase the x value by 6 using assignment operator
x += 6
print(x)

# get the module of the new x by 3
print(x % 3)



# write a simple ternary operator
# if number 8 is odd or not
odd = True if x%2 > 0 else False
print(odd)


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

