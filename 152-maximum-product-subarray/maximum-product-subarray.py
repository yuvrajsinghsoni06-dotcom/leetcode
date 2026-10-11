class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        lit,too,res = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            if curr < 0:
                lit,too = too,lit
            too = max(curr,too*curr)
            lit = min(curr,lit*curr)
            res = max(res,too)

        return res
            
        