class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans