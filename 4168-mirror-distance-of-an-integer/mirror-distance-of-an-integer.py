class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        rev = 0
        length = len(str(n))
        for i in range(1,length+1):
            rem = n % 10
            digit = 10 ** (length - i)
            rev += rem * digit
            n = n // 10

        dif = abs(original - rev)
        return dif
        