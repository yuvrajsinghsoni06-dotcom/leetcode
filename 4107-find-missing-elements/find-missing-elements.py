class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        x = min(nums)
        y = max(nums)
        return [x for x in range(x, y + 1) if x not in num_set]