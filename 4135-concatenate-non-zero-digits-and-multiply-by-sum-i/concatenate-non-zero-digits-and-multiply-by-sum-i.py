class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero = [char for char in  str(n) if int(char) != 0]

        if not non_zero:
            return 0

        x = int("".join(non_zero))

        summ = sum(int(digit) for digit in non_zero)

        return x * summ

    
                
        

        