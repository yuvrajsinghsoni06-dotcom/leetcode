class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = float('inf')
        
        # Check all possible starting indices
        for i in range(n):
            current_or = 0
            # Expand the subarray from index i to j
            for j in range(i, n):
                current_or |= nums[j]  # Bitwise OR update
                
                if current_or >= k:
                    min_len = min(min_len, j - i + 1)
                    break  # Expanding further from 'i' will only increase length
                    
        return min_len if min_len != float('inf') else -1