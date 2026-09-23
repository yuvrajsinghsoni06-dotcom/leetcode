class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        for i,num in enumerate(nums):
            if num == target:
                ans.append(i)
        return ans
