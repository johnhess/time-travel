# fib.py
def fib(n):
    # iterative Fibonaacci calculation
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fibr(n):
    # recursively calculate Fibonaacci numbers
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-1) + fibr(n-2)

for number in range(100):
    print fib(number)
