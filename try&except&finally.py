

a = 5
b = p

K=int(input('Enter the number'))
print(K)

try:

    print('Resource open')
    print(a/b)
    
except ZeroDivisionError as w:
    print("hey we can't divide the number by 0")

except ValueError as e:
    print('Invalid Input')

except Exception:
    print('Something else')

finally:
    print('Resourse closed')

print('bye')

