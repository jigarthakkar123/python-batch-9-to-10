#Function with no argument & no return value.

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python.")
printLine()

#Function with argument but no return value.

def add(a,b):
    print("Addition : ",a+b)

printLine()
add(10,20)
printLine()

#Function with argument & return value.

def sub(a,b):
    return a-b

printLine()
#ans=sub(10,20)
print("Subtraction : ",sub(10,20))
printLine()
