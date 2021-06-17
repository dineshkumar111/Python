
pos=-1

def search(nums,n):

    l=0
    u=len(nums)-1

    while l<=u:
        mid =(l+u) // 2

        if nums[mid]==n:
            globals()['pos']=mid
            return True
        
        else:
            if nums[mid]<n:
                l=mid
            else:
                u=mid

        

nums = [1,2,3,5,9,54,63,85]
n = 63

if search(nums,n):
    print('Found',pos+1)
else:
    print('not found')