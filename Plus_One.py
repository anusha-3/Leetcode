class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range (len(digits)-1, -1, -1):
            if(digits[i] < 9):
                digits[i]+=1
                return digits
            digits[i] = 0
        list = [1]
        for i in range(len(digits)):
            list.append(digits[i])
        return list