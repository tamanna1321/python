#MAP IS SOMETHING THAT VISITS EVERY VALUE AND GETS SOMETHING
#FOR LOOP IS REPLACED BY MAP
a=[12,34,56,78,89]
print(a)
def valAdd(x):
    return x**2

new=map(valAdd,[a])

new=map(lambda x:x**2,a)

# new=map(lambda x,y:x+y,[12,32,34,56,89],[11,12,13,14,15])  

print(list(new))