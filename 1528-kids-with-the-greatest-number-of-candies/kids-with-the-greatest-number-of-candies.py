class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [0 for i in range(len(candies))]
        for i , num in enumerate(candies):
            if num + extraCandies >= max_candies:
                result[i] = True
            else:
                result[i] = False

        return result