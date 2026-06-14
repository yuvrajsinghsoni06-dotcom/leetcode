class Solution:
    def partitition(self,nums):
            count = 0
            while nums != sorted(nums):
                min_idx = 0
                min_sum = nums[0] + nums[1]
                for i in range(1,len(nums)-1):
                    s = nums[i] + nums[i+1]
                    if s < min_sum:
                        min_sum = s
                        min_idx = i
                nums[min_idx: min_idx + 2] = [min_sum]
                count += 1
            return count
    

if __name__ == "__main__":
    greatone = Solution()
    nums = [5,2,3,1]
    result =greatone.partitition(nums)
    print(result)
        

        


        
        