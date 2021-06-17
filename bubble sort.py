
def sort(nums):
    
    n=len(nums)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                
                nums[j],nums[j+1] = nums[j+1],nums[j]


                


nums=[5,6,7,2,9,1]

sort(nums)
print(nums)

