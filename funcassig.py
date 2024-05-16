# WRITE A FUNCTION THAT CHECKS WHETHER A PASSED STRING IS PALIDROME OR NOT.

def is_palidrome(s):
    return s ==s[::-1]
name = "radar"
if is_palidrome(name):
    print("Your String is palidrome")
else:
    print("Your String is not palidrome")

# WRITE A PYTHON PROGRAM TO SORT A LIST OF TUPLES USING LAMBDA.

l1 = [("english",88),("social science",82),("science",90),("math",97)]
c =sorted(l1,key = lambda a :a[0]) #sorted the first element of the tuple list
d =sorted(l1,key = lambda a :a[1]) #sorted the second element of the tuple list
print(c)
print(d)

# WRITE A PYTHON PROGRAM TO SQUARE THE ELEMENTS OF  LIST USING THE MAP() FUNCTION.

def square(a):
    return a**2
a =map(square,[2,5,7,9])
print (list(a))

#GIVEN A LIST OF STRINGS WRITE A PYTHON PROGRAM TO CAPITALIZE THE FIRST LETTER 
# OF EACH STRING USING THE MAP() FUNCTION

bb= ["hello","welcome","in","python","language"]
def capitalize(bb):
    return bb.capitalize()
new = list(map(capitalize,bb))
print(new)

# WRITE A PYTHON FUNCTION THAT TAKES A LIST OF NUMBERS AND RETURN A NEW LIST 
# CONTAINING THE SQUARE ROOT OF THOSE NUMBERS USING THE MAP() FUNCTION.

import math
cc = [1,4,9,16,25]
def square_roots(cc):
    return math.sqrt(cc)
new= list(map(square_roots,cc))
print(new)
  
# WRITE A PROGRAM TO CHECK IF A NUMBER IS PRIME OR NOT

num = int(input("Enter the number :"))
count = 0
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:
            
            count += 1
            break
    if count:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

# WAP TO PRINT FIBONACCI SERIES UP TO N TERMS USING LAMBDA FUNCTION.
fibo=lambda n,a =0,b=1:[] if n==0 else[a]+fibo(n-1,b,a+b)
n = int(input("Enter any value for n: ",))
print("fibonacci series up to",n,":")
print(fibo(n))