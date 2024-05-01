class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if target==nums[i]:
        #         return i
        # return -1
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(target == nums[mid]):
                return mid
            elif(target < nums[mid]):
                r = mid-1
            elif(target > nums[mid]):
                l = mid+1
        return -1