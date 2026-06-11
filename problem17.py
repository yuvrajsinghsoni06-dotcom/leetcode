# 35. Search Insert Position - Since the question has directly instructed us that the time complexity for the following program should be log of n, we will use a binary search because our data is sorted and we have to find a logarithmic time complexity for the best and faster searching, because we are searching an element of index here. We will use a binary search operation here. 
class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            # 1. Recalculate mid INSIDE the loop so it updates as low/high change
            mid = low + (high - low) // 2
            
            # 2. Compare target to nums[mid], NOT just mid
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
                
        # 3. Return -1 if the loop finishes and the element wasn't found
        nums.insert(low,target)
        return low

# Testing the code
obj = Solution()
nums = [3, 9, 14, 19, 25, 33, 47, 56, 72, 90]
target_value = 20

result = obj.search(nums, target_value)
print(nums)

print(f"Element found at index: {result}")

        


            
        


            
        

        