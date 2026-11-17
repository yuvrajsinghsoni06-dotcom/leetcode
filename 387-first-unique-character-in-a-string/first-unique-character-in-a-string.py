class Solution:
    def firstUniqChar(self, s: str) -> int:
        coll = {}

        for ch in s:
            coll[ch] = coll.get(ch,0) + 1

        for i , ch in enumerate(s):
            if coll[ch] == 1:
                return i
        return -1
    
        