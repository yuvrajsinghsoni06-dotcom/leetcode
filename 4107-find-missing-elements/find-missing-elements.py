class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        
        # Iterate through adjacent pairs and fill in any missing gaps
        for i in range(len(nums) - 1):
            for missing in range(nums[i] + 1, nums[i + 1]):
                ans.append(missing)
                
        return ans