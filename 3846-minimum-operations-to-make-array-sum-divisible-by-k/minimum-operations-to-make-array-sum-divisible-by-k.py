class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ = sum(nums)
        operation = 0
        for i in range(k):
            if summ % k == 0:
                return operation
            else:
                summ -= 1
                operation += 1
        return operation
            
        