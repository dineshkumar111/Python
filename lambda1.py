from functools import *


lst=[1,2,3,6,5,4,8,7,9]

print(lst)

even = list(filter(lambda a : a%2==0,lst))

print(even)

double = list(map(lambda a: a*2,lst))

print(double)

sum = reduce(lambda a,b : a+b,lst)

print(sum)

