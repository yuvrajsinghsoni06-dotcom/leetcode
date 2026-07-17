class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lc = set(nums)
        longest_streak = 0
        for num in lc:
            if num - 1 not in lc:
                starting = num
                current_streak = 1

                while starting + 1 in lc:
                    starting += 1
                    current_streak +=1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak
        

        
         
                

        

        