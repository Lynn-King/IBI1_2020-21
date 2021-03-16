# recursive method

def fib_iteratively(n):
    result = 0
    if n >= 1:
        result = 1
    else:
        result = fib_iteratively(n-1) + fib_iteratively(n-2)
    return result

