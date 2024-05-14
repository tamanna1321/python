#LIST QUESTIONS
# Given a list of numbers. write a program to turn every item of a list into its square.
Given_list = [2, 5, 7, 9]
result = [x**2 for x in Given_list]
print(result)

# Concatenate two lists in the following order
Given_list1 = ["hello", "o7"]    
Given_list2 = ["world", "services"]
concatenate_list = [x + ' ' + y for x in Given_list1 for y in Given_list2]
print(concatenate_list)


# Add 10 to list after a 600

Given_list= [10, 20, [300, 400, [5000, 600], 500], 30, 50]
Given_list[2][2].append(10)
print("modified list :",Given_list)


# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item.
Given_list = [5, 10, 15, 20, 25, 30, 20, 35]
c = Given_list.index(20)
print(c)
Given_list[c] = 200
print(Given_list)