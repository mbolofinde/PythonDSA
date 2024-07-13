# Write Fibonacci series up to n 
# Write a function and pass the desired series

def fib(n):
    a, b = 0, 1
    # define the conditon
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()


