class Solution:
    def reverseString(self, s: List[str]) -> None:
        fst = 0
        lst = len(s)
        while lst > fst:
            s[fst] , s[lst-1] = s[lst-1] , s[fst]
            fst += 1
            lst -= 1
        return s

        
        