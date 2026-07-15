import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum =  n * n
        evensum = n * (n+1)

        return math.gcd(oddsum,evensum)
        