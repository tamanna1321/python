#QUESTION1.
#GIVEN A LIST OF NUMBERS .
#WAP TO TURN EVERY ITEM OF A LIST INTO ITS SQUARE.

Given_list=[13,21,12,5,6]
result=[x**2 for x in Given_list]
print (result)



#QUESTION2.
#CONCATENATE TWO LISTS IN THE FOLLOWING ORDER

Given_list1=["Hello" , "o7"]
Given_list2=["World","Services"]
concatenate_list=[x + ' ' + y for x in Given_list1 for y in Given_list2]
print(concatenate_list)



#QUESTION3. 
#ADD 10 TO LIST AFTER A 600

Given_list=[10,20,[300,400,[5000,600],500],30,50]
Given_list[2][2].append(10)
print("modified list:",Given_list)



#QUESTION4.
#YOU HAVE GIVEN A PYTHON LIST. WAP TO FIND 20 IN THE LIST.
#AND IF IT IS PRESENT REPLACE IT WITH 200. ONLY UPDATE THE FIRST OCCURENCE OF AN ITEM.

Given_list=[5,10,15,20,25,30,20,35]
c=Given_list.index(20)
Given_list.remove(20)
Given_list.insert(c,200)
print(Given_list)



#QUESTION5.
#WAP TO INPUT ELEMENTS OF THE LIST FROM THE USER AND PRINT THE SMALLEST AND GREATEST ELEMENT OF THE LIST

Ist=[]
num = int(input('How many numbers:'))
for i in range(num):
    numbers=int(input("Enter numbers:"))
    Ist.append(numbers)
a=max(Ist)
b=min(Ist) 
print(a)
print(b)  





#QUESTION6.
#WAP TO PRINT DUPLICATE FROM A LIST OF INTEGERS

input=[10,20,30,20,20,40,50,-6,-20,6,60,60,-21,-20]
a=set()
duplicate=set()
for i in input : 
    if i in a :
        duplicate.add(i)
    a.add(i)
if duplicate:
    print(duplicate)
else:
    print("No duplicate found in the list")



#QUESTION7.
#WAP TO FIND THE SECOD LARGEST NUMBER IN THE LIST

list=[60,90,20,10,50,45,30,70,32,20]
b=max(list)
final_output=list.remove(b)
c=max(list)
print(c)
        


#QUESTION8.
#WAP TO COUNT NUMBDER OF POSITIVE,NEGATIVE NUMBER AND STRINGS IN THE LIST.

list = [3,-1,5,-8,2 ,7,-4,'cherry','banana']
positive_number = 0
negative_number = 0
string = 0
for i in list:
    if isinstance (i ,(int,float)) :
        if i > 0:
         positive_number += 1
        elif  i<0:
         negative_number += 1
    elif isinstance (i,str):
        string +=1
print(positive_number)  
print(negative_number) 
print(string)     




