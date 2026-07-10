class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(num if i % 2 == 0 else -num for i, num in enumerate(nums))