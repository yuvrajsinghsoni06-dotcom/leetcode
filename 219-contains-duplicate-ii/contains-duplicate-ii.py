class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            # If element is already in current window of size k
            if num in window:
                return True
            
            window.add(num)

            # Keep window size at most k
            if len(window) > k:
                window.remove(nums[i - k])

        return False