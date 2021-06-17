
pos=-1

def search(list,n):
    
    for i in range(0,len(list),1):
        if list[i]==n:
            print('Found')
            globals()['pos']=i
        return True




list = [8,5,6,3,5,1]
n = 5

if search(list,n):
    print("Found in ")
    print(pos)
else:
    print('Not Found')