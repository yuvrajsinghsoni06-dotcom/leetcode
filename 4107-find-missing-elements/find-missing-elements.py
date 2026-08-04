class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        curr = nums[0]
        ans = []
        for num in nums:
            while curr < num:
                ans.append(curr)
                curr += 1
            curr = num + 1

        return ans
        