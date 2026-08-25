from itertools import count

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        for multiple in count(k, k):
            if multiple not in num_set:
                return multiple