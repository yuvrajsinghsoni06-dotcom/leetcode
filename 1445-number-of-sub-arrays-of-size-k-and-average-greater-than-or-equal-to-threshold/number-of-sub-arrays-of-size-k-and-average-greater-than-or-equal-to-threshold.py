class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        counter = 0
        counter = 1 if window_sum >= threshold * k else 0
        for i in range(k,len(arr)):
            window_sum += arr[i] - arr[i-k]
            if window_sum >= threshold * k:
                counter += 1
        return counter

        