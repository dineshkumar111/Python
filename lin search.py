
pos=-1

def search(list,n):

    i=0

    while i<len(list):
        if list[i]==n:
            global pos
            pos = i
            i+=1
        return True
    return False


list = [1,5,7,6,2,3]
n=6

if search(list,n):
    print("Found in ",pos)
else:
    print("Not Found")