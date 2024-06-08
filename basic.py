print("Hello World")
print(13)
print(45.0)
print(44.098)
print(type(13))
print(type(45.0))
print(type(44.098798))

#TYPE CONVERSION
a = 10
b=0
print(float(a))
print(bool(int(a)))
print(bool(b))


# Swapping two variables using third variable
a=13
b=21
temp=a
a=b
b=temp
print("a after swapping:",a)
print("b after swapping:",b)


#Swapping two variables using bitwise operators
a=5
b=6
a=a+b
b=a-b
a=a-b
print("a after swapping:",a)
print("b after swapping:",b)


#Swapping two variables using python method
a=1321
b=2113
a,b=b,a
print("After swapping")
print("value of a:",a ,"and b:",b)
