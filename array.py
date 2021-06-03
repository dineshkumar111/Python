from array import * 


s = array('i',[])

n = int(input("enter the lenght of the array"))

for i in range(n):
    x=int(input("enter the values"))
    s.append(x)

print(s)

e = 0

for i in s:
    if i == n :
        print(e)
        break

e+=1
print(s.index(n))
