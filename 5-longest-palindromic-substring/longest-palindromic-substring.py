class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        longest = s[0] # Track the longest palindrome found so far
        
        for i in range(len(s)):
            for j in range(len(s) - 1, i, -1):
                # Optimization: If the remaining distance between i and j is shorter 
                # than our longest palindrome so far, no need to check further.
                if (j - i + 1) <= len(longest):
                    break
                    
                if s[i] == s[j]:
                    left = s[i:j+1]
                    if left[::-1] == left:
                        longest = left # Update our tracker instead of returning
                        break # Break inner loop since this is the longest for this specific 'i'
                        
        return longest