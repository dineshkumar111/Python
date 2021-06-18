

def sort(nums):

    n=len(nums)

    for i in range(n-1):
        minpos=i
        for j in range(i,n):
            if nums[j]<nums[minpos]:
                minpos=j


        nums[i],nums[minpos] = nums[minpos],nums[i]


nums = [5,3,6,8,4,2,1]
sort(nums)
print(nums)