

def fib(n) :
    if n<0:
        print('please enter the correct value')
    else:    
        a = 0
        b = 1
        if n==1:
            print(a)
        else :
            print(a)
            print(b)

            for i in range(2,n):
                
                c=a+b
                if c<n :
                    a=b
                    b=c
                    print(c)    

fib(100)

