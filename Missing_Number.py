class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i
        # return len(nums)
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
        