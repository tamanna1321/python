#QUESTION1. 
# TAKE A EMPTY DICTIONARY AND ASK USER TO INPUT THE NUMBER OF TIME THEY WANT TO ENTER AND INPUT FROM
# USER TO MAKE DICTIONARY

# dict={}
# s=int(input("Enter size:"))
# for i in range(s):
#  key=input("Enter keys")
#  value=input("Enter values")
#  dict[key]=value
# print("the dictionary is")
# print(dict)
 



#QUESTION2.
#GIVEN A DICTIONARY EMPLOYEE_DETAILS WHERE THE KEYS ARE EMPLOYEE IDS AND VALUES 
#ARE DICTIONARIES WITH NAME, DEPARTMENT, AND SALARY, FILTER AND CREATE A LIST OF NAMES 
# OF EMPLOYEES WHO HAVE A SALARY GREATER THAN 50,000.

# employee_details={
# 121:{'name':'Arsh','department':'Engineering','salary':75000},
# 122:{'name':'Riya','department':'HR','salary':60000},
# 123:{'name':'Lavanya','department':'Marketing','salary':45000},
# 124:{'name':'Shanaya','department':'Finance','salary':80000},
# 125:{'name':'Vanya','department':'Doctor','salary':55000}
 
# }
# filtered_names=[details['name']for details in employee_details.values() 
#                 if details['salary']>50000]
# print("Employees with salary greater than 50000 is:",filtered_names)


 #Q3 WRITE A PROGRAM FOR A NUMBER GUESSING GAME WHERE THE COMPUTER RANDOMLY SELECTS A NUMBER 
 # BETWEEN 1 AND 100, AND THE USER TRIES TO GUESS IT. THE PROGRAM SHOULD GIVE HINTS IF 
 # THE GUESS IS TOO HIGH OR TOO LOW.

# import random

# def number_guessing_game():
#  guess_number=random.randint(1,100)
#  print("Welcome to the number guessing game!")
#  print("I habe selected a number between 1 to 100. Try to guess it")
#  attempts=0
#  while True:
#    guess=int(input("Enter your guess number(betweeen 1 to 100): "))
#    attempts+=1
#    if guess<guess_number:
#     print("Too low! Try guessing higher.")
#    elif guess>guess_number:
#     print("Too high! Try guessing lower.")
#    else:
#      print("Congratuations")
#      break
# # play_again=input("Do you want to play again:")
# # if play_again=='yes':
# #   number_guessing_game
# # else:
# #   print("Thankyou for playing")
# number_guessing_game()
  
 


# # Q4 WRITE A PROGRAM THAT CALCULATES THE DISCOUNT ON A PRODUCT BASED ON THE FOLLOWING CRITERIA:
# # IF THE PRICE IS GREATER THAN $1000, A DISCOUNT OF 10% IS APPLIED.
# # IF THE PRICE IS BETWEEN $500 AND $1000, A DISCOUNT OF 5% IS APPLIED.
# IF THE PRICE IS BELOW $500, NO DISCOUNT IS APPLIED

# def calculate_discount(a):
#  if a>1000:
#   discount=a*0.10
#  elif 500<=a<=1000:
#   discount=a*0.05
#  else:
#   discount=0
#  return discount
# def calculation():
#   price=int(input("Enter the price of the product:$"))
#   discount=calculate_discount(price)
#   final_price=price-discount
#   print(f"final price:${final_price:.2f}")
# if __name__=="__main__":
#  calculation()




 #Q5. WRITE A PROGRAM THAT CHECKS THE STRENGTH OF A PASSWORD BASED ON THE FOLLOWING CRITERIA:
# AT LEAST 8 CHARACTERS LONG
# CONTAINS BOTH UPPERCASE AND LOWERCASE CHARACTERS
# CONTAINS AT LEAST ONE DIGIT
# CONTAINS AT LEAST ONE SPECIAL CHARACTER (E.G., !, @, #, $, ETC.)

# import string
# password=input("Enter your password:")
# length=len(password)>=8
# uppercase=any(char.isupper() for char in password)
# lowercase=any(char.islower() for char in password)
# digit=any(char.isdigit() for char in password)
# special=any(char in string.punctuation for char in password)
# if length and uppercase and lowercase and digit and special:
#  strength="strong"
# else:
#  strength="weak"
#  print(f"the password'{password}' is {strength}")



#QUESTION6.
# WAP TO INSERT VALUES VALUE IN THE LIST
#LI=[20,30,40,[57,66,30,[70,80],"HELLO"],50,TRUE]
#ADD VALUE 76 BEFORE 80
#ADD VALUE 88 AFTER 57
#PRINT THE LETTER H FROM THE LIST LI

# li=[20,30,40,[57,66,30,[70,80],"Hello"],50,True]
# inner_list=li[3][3]
# inner_list.insert(1,76)
# outer_list=li[3]
# outer_list.insert(1,88)
# letter_H=li[3][5][0]
# print(li)
# print(letter_H)




#QUESTION7.
#WAP TO PLAN FOR A VACATION. TAKE INPUT FROM ASKING FOR THE BUDGET.SUGGEST MULTIPLE COUNTRIES TO 
# STAY IN THAT BUDGET.
# ASK USER TO SELECT A COUNTRY AND DISPLAY A PLACE TO VISIT IN THAT COUNTRY.
#OUTPUT
# WELCOME TO TRIP PLANNER
# ENTER YOUR BUDGET (5000-10000, 10000-20000, 20000-30000, 30000-40000)
# 25000
#COUNTRY AVAILABLE UNDER 30000 ARE:
# INDIA
# AUSTRALIA
# USA
#SELECT YOUR CHOICE: INDIA
# THE PLACE TO VISIT IN THE INDIA IS THE TAJ MAHAL



print("Welcome to the trip planner")
budget=int(input("Enter your budget(5000-10000,10000-20000,20000-30000,30000-40000):"))
available_countries=[]
if 5000<=budget<10000:
 available_countries=["thailand","indonesia"]
 print ("Countries avaialble on your budget are :Thailand,Indonesia")
elif 10000<=budget<20000:
 available_countries=["japan","spain"]
 print("Countries avaialble on your budget are :Japan,Spain")
elif 20000<=budget<30000:
 available_countries=["india","australia","usa"]
 print ("Countries avaialble on your budget are :India,Australia,USA")
elif 30000<=budget<40000:
 available_countries=["mexico","dubai"]
 print ("Countries avaialble on your budget are :Mexico,Dubai")
else:
 print("No countries available for entered budget")
 exit()
selected_country=input("Select your choice:").strip().lower()
if selected_country in available_countries:
 if selected_country=="india":
  print("Golden Temple")
 elif selected_country=="thailand":
  print("Phuket")
 elif selected_country=="indonesia":
   print("Bali")
 elif selected_country=="japan":
   print("Mount Fuji")
 elif selected_country=="spain":
  print("La Sagrada Familia")
 elif selected_country=="australia":
  print("Sydney")
 elif selected_country=="usa":
  print("Statue Of Liberty")
 elif selected_country==("mexico"):
  print("Todos Santos Island")
 elif selected_country=="dubai":
  print("Burj Khalifa")
else:
 print("Sorry No Places To Visit In That Country")
