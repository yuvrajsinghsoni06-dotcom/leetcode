
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        m = str(n)
        summ = 0
        for i in m:
            summ += int(i)

        return summ
            

        