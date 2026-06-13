# 169. Majority Element

class Solution:
    def majorityelement(self,nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count +=1 if num == candidate else -1

        return candidate


        

# testing

if __name__ == "__main__":
    greatone = Solution()
    nums = [3,2,3]
    result =greatone.majorityelement(nums)
    print(result)

