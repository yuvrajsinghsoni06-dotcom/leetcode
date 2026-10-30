class Solution {
    public int findMin(int[] nums) {
        int left = 0 , right = nums.length -1;
        while (left < right) {
           int mid = left + (right - left) / 2;

    // Compare middle element with the rightmost element
           if (nums[mid] > nums[right]) {
        // The minimum must be in the right half
              left = mid + 1;
            } else {
        // The minimum is at mid or in the left half
              right = mid;
    }
        }

    return nums[left];
    }
}