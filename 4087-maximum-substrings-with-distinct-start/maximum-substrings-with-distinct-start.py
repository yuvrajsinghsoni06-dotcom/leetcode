class Solution:
    def maxDistinct(self, s: str) -> int:
        ans = []
        for char in s:
            if char not in ans:
                ans.append(char)
            else:
                continue
        return len(ans)

        