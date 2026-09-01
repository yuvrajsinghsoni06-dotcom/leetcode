class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res , summ = nums[0], nums[0]
        for i in range(1,len(nums)):            
            summ = max(nums[i], summ + nums[i])
            res = max(res,summ)
            if summ < 0:
                summ = 0
            

        return res


        