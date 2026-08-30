class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)

        case1 = j + 1
        case2 = len(nums) - i
        case3 = (i + 1) + (len(nums) - j)


        return min(case1,case2,case3)




        