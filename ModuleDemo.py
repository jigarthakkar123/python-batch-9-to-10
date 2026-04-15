import udf

while True:

    print("*"*40)
    print("1. OddEven")
    print("2. Max Of Two Number")
    print("3. Max Of Three Number")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*40)
    choice=int(input("Enter Your Choice : "))
    print("*"*40)

    if choice==1:
        n1=int(input("Enter Number : "))
        udf.oddeven(n1)
    elif choice==2:
        n1=int(input("Enter Number : "))
        n2=int(input("Enter Number : "))
        udf.maxoftwo(n1,n2)
    elif choice==3:
        n1=int(input("Enter Number : "))
        n2=int(input("Enter Number : "))
        n3=int(input("Enter Number : "))
        udf.maxofthree(n1,n2,n3)
    elif choice==4:
        n1=int(input("Enter Number : "))
        udf.fibonacci(n1)
    elif choice==5:
        n1=int(input("Enter Number : "))
        udf.prime(n1)
    elif choice==6:
        print("Thank You For Using Our Services.")
        print("*"*40)
        break
    else:
        print("Invalid Choice. Please Try Again.")
    print("*"*40)
        
    
