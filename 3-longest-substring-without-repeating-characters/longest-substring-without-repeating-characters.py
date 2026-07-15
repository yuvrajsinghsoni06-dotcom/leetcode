class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A set provides O(1) instant lookups to see if a character is in our window
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If we hit a duplicate, shrink the window from the left 
            # until the duplicate is no longer inside
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current valid character to our window's memory
            char_set.add(s[right])
            
            # Record the length of the window if it's our new high score
            # The length of the window is simply (right pointer - left pointer + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length