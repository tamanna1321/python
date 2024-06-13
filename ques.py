#CREATE A PROGRAM  
# ASK INPUT FROM USER
#ENTER NAME-TAMANNA
#ENTER AGE-19
#ENTER DAY-21
#ENTER MONTH NUMBER-5
#IN THE END PRINT THANKS FOR ALL THE INPUTS. I AM A MAGICIAN. HEY TAMANNA YOU WERE BORN ON 21 MAY 2005
name=input("Enter your name:")
age=int(input("Enter your age:"))
day_of_birth=int(input("Enter day of birth:"))
month=int(input("Enter month number from (1-12):"))
current_year=2024
year_of_birth=current_year-age
month_names = ["January","February","March","April",
               "May","June","July","August","September",
               "October","November","December"] 
birth_month=month_names[month -1]
print(f"hey{name},you were born on {birth_month} {day_of_birth},{year_of_birth}")









#ASK USER TO INPUT TWO NUMBERS a AND b. CREATE A LOOP AND PRINT THE NUMBER IN THE LOOP,
#MAKE SURE IF b IS SMALLER THAN  a THEN GENERATE REVERSE LOOP
#1st:10
#2nd:17
#10 11 12 13....16
#1st:17
#2nd:10
#17 16 15 14 13 .....11




a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a<b:
    for i in range(a,b):
     print(i)
else:
   for i in range(a,b,-1):
      print(i)