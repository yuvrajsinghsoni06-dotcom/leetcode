class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_str = float('inf')
        n = len(nums)
        for i in range(n):
            current = 0
            for j in range(i,n):
                current |= nums[j]
                if current >= k:
                    min_str =min(min_str,j - i + 1)
        return min_str if min_str != float('inf') else -1
        