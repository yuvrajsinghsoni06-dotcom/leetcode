class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum , leftsum = 0,0
        total_sum = sum(nums)
        for i in range(len(nums)):
            rightsum = total_sum - leftsum - nums[i]
            if rightsum == leftsum:
                return i
            else:
                leftsum += nums[i]

        return -1

        