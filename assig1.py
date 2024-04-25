#QUESTION 1
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return ‘not a valid string’ instead of the empty string


a = input("Enter a string ")
if len(a)<2:
    print("not a valid String")
else:
 b=a[:2]+""+a[-2:]
print(b)


#QUESTION 2
# Write a Python program to get a single string from two given strings, separated by a space and
# swap the first characters of each string


str1 = input("Enter str1 ")
str2 = input("Enter str2 ")
a= str1.replace(str1[0],str2[0])
print(a)
b=str2.replace(str2[0],str1[0])
print(b)
result =a+" "+b
print(result)


# QUESTION 3
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged


a = input("Enter the string :")
if len(a)>=3:
    if a.endswith('ing'):
      result = a+ 'ly'
    else:
       result = a + 'ing'
else:  
   result = a
print(result)


#QUESTION 4
# Write a Python program to remove the nth index character from a nonempty string
# Write a Python program to remove the characters which have odd index values of a given string.
# Swap commas and dots in string.


a= input("Enter a string")
n = int(input("Enter the index to remove"))
result1 = a[:n] + a [n+1:]
result2 = ''
for i in range(len(a)):
   if i % 2 == 0:
    result2 +=a[i] 
result3 = a.translate(str.maketrans('.,',',.'))
print("a",a)
print("output1:",result1)
print("output2:",result2)
print("output3:",result3)

   