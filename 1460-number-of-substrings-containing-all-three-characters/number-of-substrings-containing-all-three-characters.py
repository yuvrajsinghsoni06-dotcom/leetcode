class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {"a" : 0 , "b": 0 , "c": 0}
        left = 0
        ans = 0
        for i in range(0,len(s)):
            counter[s[i]] += 1

            while counter["a"] > 0 and counter["b"] > 0 and counter["c"] > 0:

                ans += len(s) - i

                counter[s[left]] -= 1
                left += 1

        return ans

        

        


        