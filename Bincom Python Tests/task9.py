# QUE9: Write a program to sum the first 50 fibonacci sequence.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_sum = sum(fibonacci(i) for i in range(1, 51))
print(f"The sum of the first 50 Fibonacci numbers is: {fibonacci_sum}")
