class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        start, max_length = 0, 1
        
        def expand_around_center(left: int, right: int) -> None:
            nonlocal start, max_length
            # Expand outward as long as boundaries are valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                # If we found a longer palindrome, track its start and length
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

        for i in range(len(s)):
            # Case 1: Odd length palindromes (center is at i)
            expand_around_center(i, i)
            # Case 2: Even length palindromes (center is between i and i+1)
            expand_around_center(i, i + 1)
            
        return s[start : start + max_length]