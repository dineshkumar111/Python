
def count(n):
    even = 0
    odd = 0

    for i in lst:

        if i%2==0:
            even+=1
        else :
            odd+=1 

    print(even,odd)
    return even,odd


lst = []
n=int(input('enter the number'))

for i in range(0,n):
    elements =int(input())

    lst.append(elements)
print(lst)
even, odd = count(lst)





