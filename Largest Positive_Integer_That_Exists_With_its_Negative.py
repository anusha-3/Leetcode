class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l = []
        ans = -1
        for i in nums:
            if -i in l:
                ans = max(ans, abs(i))
            l.append(i)
        return ans