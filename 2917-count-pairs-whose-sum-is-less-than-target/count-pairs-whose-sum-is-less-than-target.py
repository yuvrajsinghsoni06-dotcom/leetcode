class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
           for j in range(i+1,n):
            total = nums[i] + nums[j]
            if total < target:
                count +=1

        return count
    
            
