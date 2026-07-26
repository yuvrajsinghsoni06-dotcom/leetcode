class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        maxx = 0
        n = len(nums)
        for i in range(k):
            curr += nums[i]
        maxx = curr
        for j in range(1,n-k+1):
            curr = curr - nums[j-1] + nums[j + k - 1]
            if curr > maxx:
                maxx = curr
        return maxx / k
        
