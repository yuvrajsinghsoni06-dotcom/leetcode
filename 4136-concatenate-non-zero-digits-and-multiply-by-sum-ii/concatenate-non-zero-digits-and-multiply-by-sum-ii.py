class Solution:
    def __getattr__(self, name):
        return self.solve
        
    def solve(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        pref_val = [0] * (n + 1)
        pref_sum = [0] * (n + 1)
        cnt = [0] * (n + 1)
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        for i in range(n):
            val = int(s[i])
            if val > 0:
                pref_val[i + 1] = (pref_val[i] * 10 + val) % MOD
                pref_sum[i + 1] = pref_sum[i] + val
                cnt[i + 1] = cnt[i] + 1
            else:
                pref_val[i + 1] = pref_val[i]
                pref_sum[i + 1] = pref_sum[i]
                cnt[i + 1] = cnt[i]
                
        ans = []
        for l, r in queries:
            c = cnt[r + 1] - cnt[l]
            if c == 0:
                ans.append(0)
            else:
                s_val = pref_sum[r + 1] - pref_sum[l]
                v_val = (pref_val[r + 1] - pref_val[l] * pow10[c]) % MOD
                ans.append((v_val * s_val) % MOD)
                
        return ans