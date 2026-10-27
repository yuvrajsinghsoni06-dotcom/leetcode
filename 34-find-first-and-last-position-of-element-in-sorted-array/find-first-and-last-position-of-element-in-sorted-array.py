class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def firstone(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # Keep searching left for the first occurrence
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return first

        def Secondone(nums, target):
            low, high = 0, len(nums) - 1
            sec = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    sec = mid
                    low = mid + 1  # Keep searching right for the last occurrence
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return sec

        return [firstone(nums, target), Secondone(nums, target)]