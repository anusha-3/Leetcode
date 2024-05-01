class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        wordList = list(word)
        index = 0
        c = 0
        ans = []
        if ch in wordList:
            index = wordList.index(ch)
        for i in range(len(wordList)):
            if i <= index:
                ans.append(wordList[index-c])
                c += 1
            else:
                ans.append(wordList[i])
        return ''.join(ans)