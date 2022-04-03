class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:     # 逆序删除
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)


    def removeDuplicates2(self, nums: List[int]) -> int:     # 双指针
        if not nums:
            return 0
        n = len(nums)
        right = 1
        left = 0
        while right < n:
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1
            right += 1
        return left + 1