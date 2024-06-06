#QUESTION 1:

# WAP ASK USER TO INPUT A NUMBER AND THEN MONTH NAME CORRESPONDING TO THAT NUMBER 
month_names = ["January","February","March","April",
               "May","June","July","August","September",
               "October","November","December"] 

number = int(input("Enter a number(1-12):"))

if 1<= number <= 12:
   print("The month corresponding to that number is:",month_names[number-1])
else:
   print("invalid number.")   


#QUESTION 2:

#WAP ASK USER TO INPUT 2 NUMBER
#TELL THE FOLLOWINGS
#1. BOTH NUMBERS ARE EQUAL OR NOT
#2. WHICH IS BIGGER IN BOTH NUMBERS
#3. EITHER 1ST NUMBER IS SMALLER OR EQUAL TO 2ND NUMBER
#4. PRINT YOUR FIRST NAME 5 TIMES IF 1ST NUMBER IS GREATER THAN 2ND NUMBER
#5. PRINT YOUR SURNAME IF 1ST NUMBER IS LESS THAN 2ND NUMBER


num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

# Both number are equal or not

if num_1 == num_2 :
   print(" Both numbers are equal.")
else :
   print("Both numbers are not equal.") 

#Which is Bigger in both 

if num_1 > num_2 :
   print("First number is Bigger.") 
elif num_2 > num_1:
  print("Second number is Bigger.") 
else :
   print("Both are equal.") 

# Either First Number is smaller or equal to Second Number

if num_1 <= num_2:
   print("First Number is smaller or equal to Second Number")
else:
   print("First Number is greater or equal to Second Number") 

# Print your first name 5 times is first number is greather than second and 
# print your surname 3 times if 1st no is less than second..

if num_1 > num_2:
   print("your first name" * 5) 
elif num_1 < num_2:
   print("your surname " * 3) 

#QUESTION 3:

#USING USER INPUT ASK THE USER TO INPUT 2 STRINGS AND TELL FOLLOWINGS 
#1. USING == TELL BOTH STRINGS ARE EQUAL OR NOT
#2. USING IS OPERATOR TELL BOTH STRINGS ARE EQUAL OR NOT 

string1 = input("Enter the first string") 
string2 = input("Enter the second string") 

if string1 == string2:
   print("Using '==' : Both strings are equal") 
else :
   print("Using '==': Both strings are not  equal") 

if string1 is string2:
   print("Using 'is' : Both strings are not equal")  
else:
   print("Using 'is': Both strings are  equal")   

#QUESTION 4:

#ASK USER TO INPUT 2 STRINGS AND CONVERT IT INTO NUMBERS AND USING IS OPERATOR TELL BOTH ARE EQUAL OR NOT

num1 = int(input("Enter first number as a string:"))    
num2 = int(input("Enter second number as a string:"))   
if num1 is num2:
   print("Using 'is' : Both numbers  are equal") 
else:
   print("Using 'is' : Both numbers are not equal")    


#QUESTION 5:
#CREATE A MENU DRIVEN PROGRAM TO PERFORM THE CALCULATOR AS BELOW 
# OP WELCOME TO SADA CALCULATOR SELECT YOUR CHOICE
#1. ADDITION
#2. SUBTRACTION
#3. DIVISION
#4. MULTIPLICATION
#5. POWER
#6. REMAINDER 


# ----> 2
#ENTER 1ST NUMBER:100
#ENTER 2ND NUMBER:300
#SUB IS:-200  

print("Welcome to Sada Calculator")
print("Select your choice")
print()
print("1. Addition")
print("2. Substration")
print("3. Division")
print("4. Multiplication")
print("5. Power")
print("6. Reminder")
choice = int(input(" ---> "))
if choice == 1:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    result = num_1+num_2
    print("sum is",result)

elif choice == 2:
   num_1 = float(input("Enter first number:"))
   num_2 = float(input("Enter second number:"))
   result = num_1-num_2
   print("difference is",result)

elif choice == 3:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    if num_2 != 0:
     result = num_1 / num_2
     print("division is",result)  
    else :
     print("Cannot divide by zero")
elif choice == 4:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    result = num_1*num_2
    print("Multiplication  is",result)  
elif choice == 5:
    num_1 = float(input("Enter the base  number:"))
    num_2 = float(input("Enter exponent  number:"))
    result = num_1**num_2
    print("power is",result)
elif choice == 6:
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))
    result = num_1%num_2
else :
   print("invalid choices..")  

#QUESTION 6:

#Ask USER TO INPUT A NUMBER WITH + OR - AND PERFORM FOLLOWINGS 
#OP ENTER A NO: 567
#ENTER OP(+,-):+0,1,2,3......566
#IF - 567........>......1

number =int(input("Enter a number ")) 
operations = input("Enter OP from + or -")
if operations == "+":
 result = [i for i in range(0,number)]
elif operations == "-" :
 result = [i for i in range(number,0,-1)]
else :
  result ="invalid number"
print(result) 

#QUESTION 7:

#ASK USER TO INPUT A NUMBER AND TELL ALL EVEN NUMBER UPTO THAT NUMBER
#EG: INPUT A NUM: 29
#EVEN ARE:2,4,6,8,......28

user_num = int(input("Enter a number:"))
for i in range(2,user_num+1):
  if i % 2 == 0:
   print(i)
