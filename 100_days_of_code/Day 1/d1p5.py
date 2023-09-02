a=input("A is :")
b=input("B is :")
c=a
a=b
b=c
#c--a--a---b--b---c
print("A is now:" + a)
print('B is now:' + b)

print(type(a))

#this is actually a string as we have given input
#this is not int although it feels like one
#adding a string and a int is not possible in python