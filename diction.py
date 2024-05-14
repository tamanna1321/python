#WAP TO CREATE FOLLOWING STRUCTURE
# SAMPLE LISTS["BLACK","RED","MAROON","YELLOW"]
colour_name=["Black","Red","Maroon","Yellow"]
colour_code=["#000000","FF0000","#800000","#FFFF00"]
result=[{"colour_name":colour_name[i],"colour_code":colour_code[i]}
        for i in range(len(colour_name))]
print(result)


#WAP TO FIND THE SUBJECT WITH SECOND HIGHEST MARKS IN {'ENG':100,'HINDI':20,'SOCIAL':45,'PUNJABI':85}
marks={'eng':100,'hindi':20,'social':45,'punjabi':85}
print("highest marks:",sorted(marks.values())[-1])
print("second highest marks:",sorted(marks.values())[-2])

# WAP TO  CREATE FOLLOWING LIST
# a = ['a','b','c']
# b = ['d','e','f']

a = ['a','b','c']
b = ['d','e','f']
result = [a+b for a,b in zip(a,b)]
print(result)
