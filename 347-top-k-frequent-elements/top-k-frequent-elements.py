class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1

        sorted_arr = sorted(counter.items(),key=lambda x:x[1], reverse=True)
        return [num for num , count in sorted_arr[:k]]
        