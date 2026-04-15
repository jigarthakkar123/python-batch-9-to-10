def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial Of ",5," Is : ",factorial(51))
print(type(factorial(51)))
