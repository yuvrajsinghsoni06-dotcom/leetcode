class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        soln = [0] * n
        if k == 0:
            return soln

        for i in range(n):
            if k > 0:
                soln[i] = sum(code[(i + j) % n] for j in range(1,k+1))
            elif k < 0:
                soln[i] = sum(code[(i - j) % n] for j in range(1, abs(k) + 1))

        return soln

        
            
        