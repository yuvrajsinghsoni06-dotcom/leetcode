class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(1,len(s)):
            prev= ord(s[i-1])
            after = ord(s[i])
            total += abs(prev - after)
        return total

            

        