def cube(x):
    return x*x*x

print("Cube Of 5 Is : ",cube(5))

ans=lambda y:y*y*y
print("Cube Of 5 Is : ",ans(5))

x=lambda a,b:a+b
print(x(10,20))


def oddeven(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")

oddeven(5)

y=lambda a:"Even" if a%2==0 else "Odd"
print(y(5))
