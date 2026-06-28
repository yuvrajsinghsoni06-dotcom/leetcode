from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        visited = set()
        
        # 1. Correctly handle the 1s edge case
        ones = count.get(1, 0)
        answer = ones if ones % 2 != 0 else ones - 1
        answer = max(1, answer)  # Ensure minimum length is 1
        
        # Skip 1 in the main loop logic
        visited.add(1)

        # 2. Main sequence builder
        for x in count:
            if x in visited:
                continue
                
            current = x
            chain_length = 0
            
            while count[current] >= 2:
                visited.add(current)
                chain_length += 1
                nxt = current * current
                
                # If the next square is missing entirely, we can't use 
                # the current element as a pair; it must become the peak.
                if nxt not in count:
                    chain_length -= 1
                    break
                    
                current = nxt
            
            total = chain_length * 2 + 1
            answer = max(answer, total)
        
        return answer