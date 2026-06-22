# 1189. Maximum Number of Balloons


class Solution:
    def maxBalloon(self,text: str):
        count ={"b" : 0 , "a" : 0 , "l" : 0, "o" : 0,  "n":0}
        for char in text:
            if char in count:
                count[char] += 1
            
        count["l"] = count["l"] // 2
        count["o"] = count["o"] // 2

        return min(count["b"], count["a"] , count["l"] ,  count["o"] , count["n"])


if __name__ == "__main__":
   sol = Solution()
   text = "loonbalxballpoon"
   result = sol.maxBalloon(text)
   print(result)
        

