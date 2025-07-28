number = int(input("Enter the no for calculating recursion\n"))

def factorial_fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return factorial_fibonacci(n-1) + factorial_fibonacci(n-2)

print(factorial_fibonacci(number))

