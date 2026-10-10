class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maax = nums[0]
        mini = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            if curr < 0:
                maax , mini = mini,maax
            maax = max(curr,maax*curr)
            mini = min(curr,mini*curr)
            res = max(res,maax)

        return res