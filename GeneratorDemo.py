def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Create the Fibonacci generator
fib = fibonacci(50)

# Iterate and print the Fibonacci numbers

print(list(fib))

