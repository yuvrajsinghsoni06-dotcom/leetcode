class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))
        rank = {}
        for i , num in enumerate(nums):
            rank[num] = i + 1
            
        return [rank[num] for num in arr]
        


        