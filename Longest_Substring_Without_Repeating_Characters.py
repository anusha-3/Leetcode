class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = i = 0
        ss=set()
        for j, c in enumerate(s):
            while c in ss:
                ss.remove(s[i])
                i+=1
            ss.add(c)
            ans = max(ans, j-i+1)
        return ans