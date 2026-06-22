# 1189. Maximum Number of Balloons


class Solution:
    def maxBalloon(self,text: str):
        if not text:
           return 0
        count = 0
        collection = ["b","a","l","l","o","o","n"]
        for char in text:
            if char in collection:
                collection.remove(char)
            else:
                continue
        if len(collection) == 0:
               count +=1
        else:
            return 
        return count


if __name__ == "__main__":
   sol = Solution()
   text = "loonbalxballpoon"
   result = sol.maxBalloon(text)
   print(result)
        

