#QUESTION1.
#WAP IN PYTHON THT TAKES TWO STRINGS INPUT 's1' AND 's2' FROM USER
# AND RETUEN A STRING CONTAINING THE APPEAR IN BOTH STRING
#1. ("hello", "world") #lo
#2.  ("abc","def") #""

s1= input("enter the first string ")
s2= input("enter the second string ")
common= ""
for char in s1:
 if char in s2 and char not in common:
  common+=char
print(common)


#QUESTION2.
#WAP IN PYTHON THAT TAKES SENTENCE AS INPUT AND RETURNS NUMBER OF WORDS IN SENTENCE.
#WORDS ARE SEPERATED BY SPACES

sentence= input("Enter a sentence :")
print(len(sentence.split()))


#WAP ON PYTHON TO CHECK IF TWO STRINGS 's1' AND 's2' ARE ROTATION OF EACH OTHER 
#a. ("hello","lohel") #True
#b. ("hello","world") #False

def are_rotations(s1,s2):
 if len(s1)!=len(s2):
  return False
  s3=s1+s1
  if s2 in s3:
   return True
  else:
   return False
s1=input("Enter the first string")
s2=input("Enter the second string")
  
if are_rotations(s1,s2):
 print("They are rotations of each other..")
else:
   print("They are not rotations of each other..")


   #WAP IN PYTHON THAT TAKES A STRING AS INPUT AND RETURNS TJE CHARACTER THAT APPEARS MOST FREQUENTLY.
   #IF THERE ARE MULTIPLE CHARACTERS WITH THE SAME MAXIMUM FREQUENCY,RETURN ANY ONE OF THEM.

   str=input("Enter a string:")
   l=list (str)
   print(l)
   freq=[l.count(ele)for ele in l]
   print(freq)
   d=dict(zip(l,freq))
   print(d)


   #WAP IN PYTHON THAT CONVERTS A STRING FROM snake_case TO CamelCase

   snake_case=input("Enter a string in snake case")
   a=snake_case.split(" ")
   camel_case= a[0] +''.join(x.title()for x in a[1:])
   print(camel_case)
