class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        counts_map = {}  # This is our hash map
        
        for num in nums:
            # If we've seen this number before, add its current frequency to our pairs
            if num in counts_map:
                count += counts_map[num]
                counts_map[num] += 1
            else:
                # First time seeing this number
                counts_map[num] = 1
                
        return count