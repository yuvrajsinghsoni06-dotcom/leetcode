class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        # 1. Pre-process the string to handle even/odd lengths uniformly
        # e.g., "babad" -> "^#b#a#b#a#d#$"
        # '^' and '$' act as unique bounds to prevent index out of bounds checks
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n  # Array to store palindrome radii
        C = R = 0    # Center and Right boundary of the furthest palindrome
        
        for i in range(1, n - 1):
            # Find the mirror of index i with respect to center C
            i_mirror = 2 * C - i
            
            # If within the current right boundary, copy the mirrored radius
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            
            # Attempt to expand the palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            
            # If the expanded palindrome extends beyond R, adjust C and R
            if i + P[i] > R:
                C = i
                R = i + P[i]
        
        # 2. Find the maximum radius and its center index in the transformed array
        max_len, center_index = max((val, idx) for idx, val in enumerate(P))
        
        # 3. Map the center and radius back to the original string indices
        start = (center_index - 1 - max_len) // 2
        return s[start : start + max_len]