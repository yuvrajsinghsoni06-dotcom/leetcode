class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        res,amount = 0,0
        m = len(accounts)
        n = len(accounts[0])
        for i in range(m):
            amount = 0
            for j in range(n):
                amount +=accounts[i][j]
            res = max(res,amount)
        return res

        