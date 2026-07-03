class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the list from the last element down to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No more carry needed, we can stop and return
            
            # If it is 9, it becomes 0, and the loop continues to the next element on the left
            digits[i] = 0
            
        # If the loop finishes, it means all digits were 9 (e.g., [9, 9] -> [0, 0])
        # We just need to prepend 1 at the very beginning
        return [1] + digits