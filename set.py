# SETS  ARE MADE BY {}
#CONTAINS UNIQUE ELEMENTS,ARE UNINDEXED,ARE UNORDERED
# sets are made by {}
# It contains unique elements..
# It is unindexed and unordered
a={12,34,56,78,34,12}
print(a)

# print(a[2])  -- shows error 

a.add(11)
a.add(30)  # add use only single element

a.update({23,45,89})   # update used for add multiple elements in sets

print(a)
a = {12,23,34,56,78}
a.remove(34)
#a.remove(91) #shows exception if element is not present..
print(a)
a.discard(34)
a.discard(91) # it will not show any exception if the the element is not present..
print(a)
# a.clear()
# print(a)
a.copy()
print(a)
a ={1,2,13,21,True,23.21}
b={21,13,5,6,1}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.isdisjoint(b))