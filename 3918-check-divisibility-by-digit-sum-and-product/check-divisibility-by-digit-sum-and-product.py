class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ, product = 0,1
        length = len(str(n))
        digit = n
        while length != 0:
            rem = n % 10
            summ += rem 
            product *= rem
            n = n // 10
            length -= 1

        if digit % (summ + product) == 0:
            return True
        else:
            return False
        

        

        