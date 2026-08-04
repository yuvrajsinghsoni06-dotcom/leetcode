class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x = min(nums)
        y = max(nums)
        llist = []
        for i in range(x,y+1):
            if i not in nums:
                llist.append(i)
        return sorted(llist)