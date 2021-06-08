
def fib(n):

    if n==0:
        return 1
    else:
        return n*fib(n-1)
     


result = fib(5)

print(result)