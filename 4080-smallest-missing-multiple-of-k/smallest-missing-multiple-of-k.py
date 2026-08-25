class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        soln = set(nums)
        ans = k
        while ans in soln:
            ans += k
        return ans
                

       