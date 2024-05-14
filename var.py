#VARIABLES
#LOCAL AND GLOBAL SCOPE

x=10
print("Before func:",x)

def check():
    global x 
    x=20 #LOCAL VARIABLE
print("Inside function",x)

check()
print("After function",x)