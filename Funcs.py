#FUNCTIONS ARE OF TWO TYPES:USER DEFINED AND PRE DEFINED
#PRE DEFINED EX: print(),input()
#USER DEFINED EX: def

def sums():
    print("Hello, I'm function")
    return "hi"
print(sums())


def sums(a,b):   #-- Parameters
    print(a+b)
    
    return a+b
    
a=sums(11,12)   #  arguments
print(a)

def sums(a,b):   #-- Parameters
    # print(a+b)
    return a+b
i=int(input('Enter i '))
j=int(input('Enter j '))
a=sums(i,j)   #  arguments
print(a)


def defVal(a,b=20):
    print(a,b)
    
defVal(12,55)


def OddEven(x):
    if x%2==0:
        return "Even"
    else:
        return "Odd"

num=int(input("Enter number "))

print(OddEven)
c=90
d=90
print(id(c))
print(id(d))




#FUNCTIONS WITH KEYWORD ARGUMENTS

def prntVal(a,b,c):
    print(a,b,c)
    
    
prntVal(12,b=10,c=20)

print("hello \\n  hi")


def arbPrint(*a):
    # print(a)
    sum=0
    for i in a:
        sum+=i
    print(sum)    
    
    
arbPrint(12,34,45,67,44,221)


#TUPLE IN PYTHON
x=(12,'hi',True,9.9)
print(x)
print(type(x))


x=list(x)
x[1]=23
x=tuple(x)
print(x)



    