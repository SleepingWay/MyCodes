nums = [1,2,3,4,5,6,7]
k = 3
nums[:] = nums[::-1]
nums[:k] = nums[k-1::-1]
nums[k:] = nums[:k-1:-1]
print(nums)