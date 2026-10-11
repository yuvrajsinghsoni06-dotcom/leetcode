class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        coll = {}
        for i in range(len(nums)):
            complementary = target - nums[i]
            if complementary in coll:
                return [i,coll[complementary]]
            coll[nums[i]] = i

        