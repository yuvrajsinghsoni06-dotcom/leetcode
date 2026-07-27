class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        seq = [0] * n

        if k == 0:
            return seq

        if k > 0:
            right ,left = k, 1
        elif k < 0:
            right , left = n - 1, n - abs(k)

        window = sum(code[i % n] for i in range(left, right+1))

        for i in range(n):
            seq[i] = window

            window -=code[left % n]
            left += 1
            right += 1
            window += code[right % n]

        return seq
        