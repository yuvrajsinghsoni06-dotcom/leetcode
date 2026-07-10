class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        summ = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                summ += num
            else:
                summ -= num
        return summ
        