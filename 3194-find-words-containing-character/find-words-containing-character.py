class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count = 0
        ans = []
        for ch in words:
            if x in ch:
                ans.append(count)
            count += 1

        return ans
            
        