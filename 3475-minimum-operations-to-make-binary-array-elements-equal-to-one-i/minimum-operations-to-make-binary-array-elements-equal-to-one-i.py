class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = 3
        
        # is_flipped[i] tracks if a k-size flip WAS STARTED at index i
        is_flipped = [0] * n
        
        flipped_count = 0  # Number of active flips affecting nums[i]
        operations = 0

        for i in range(n):
            # 1. Slide the window: remove the flip that started at i - k
            if i >= k:
                flipped_count ^= is_flipped[i - k]

            # 2. Check current element's actual state after applying active flips
            current_val = nums[i] ^ flipped_count

            # 3. If it's 0, we MUST flip starting at index i
            if current_val == 0:
                # If there aren't k elements left, it's impossible!
                if i + k > n:
                    return -1
                
                is_flipped[i] = 1
                flipped_count ^= 1
                operations += 1

        return operations