
nums = [5,6,8,4]

it=iter(nums)

print(next(it))

print(it.__next__())

for i in nums:
    print(i)