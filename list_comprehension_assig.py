#QUESTION1.
#USING LIST COMPREHENSION FIND ALL THE NUMBERS FROM 1 TO 1000 THAT ARE DIVISIBLE BY 7

list=[i for i in range(1,1000) if i%7==0]
print(list)



#QUESTION2.
#COUNT THE NUMBER OF SPACES IN A STRING USING LIST COMPREHENSION

s="python is a high level programming language"

space=[ i for i in s if i == ' ']
print(len(space))



#QUESTION3.
#USING LIST COMPREHENSION FIND THE COMMON NUMBERS IN TWO LISTS WITHOUT USING A TUPPLE OR SET 
#l1=[1,2,3,4]
#l2=[2,3,4,5]

list1=[1,2,3,4]
list2=[2,3,4,5]
in_list2=[x for x in list1 if x in list2]
print(in_list2)



#QUESTION4.
#GIVEN NUMBERS RANGE(0,20),PRODUCE A LIST CONTAINING THE WORD EVEN IF A NUMBER IN THE NUMBERS IS EVEN,
#AND THE WORD ODD IF THE NUMBER IS ODD.USING LIST COMPREHENSION.
#RESULT WOULD LOOK LIKE 'odd','even','odd','even'......

result = ['even' if i %2 ==0 else 'odd' for i in range(20)]
print(result)



#QUESTION5.
#USING LIST COMPREHENSION FIND ALL THE WORDS IN A STRING LESS THAN 4 LETTERS

words=["books","language","bat","mat","tree","hat","python"]
words_in_string=[i for i in words if len(i)<4]
print(words_in_string)



#QUESTION6.
#USING LIST COMPREHENSION PRODUCE A LIST OF TUPPLES CONSISTING OF ONLY THE MATCHING NUMBERS IN THE LIST
#a=[1,1,3,4,5,6]
#b=[5,6,7,8,9]
#RESULT WOULD LOOK LIKE(5,5),(6,6)

a1=[1,2,3,4,5,6,7,8,9]
b1=[2,7,1,12]
result = [(a,b)for a in a1 for b in b1 if a==b]
print(result)


