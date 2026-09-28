class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2.sort()
        a = set()
        for num in nums1:
            left, right = 0, len(nums2) -1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] == num:
                  a.add(num)
                  break
                elif num < nums2[mid]:
                  right = mid -1
                else:
                  left = mid +1

        return list(a)

                

        