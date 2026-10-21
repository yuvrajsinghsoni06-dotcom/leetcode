class Solution {
    public int maxProductDifference(int[] nums) {
        int n = nums.length;
        int low = 0;
        int high = n - 1;
        
        // Partition logic (single-pass Lomuto partition around the last element pivot)
        int pivot = nums[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (nums[j] <= pivot) {
                i++;
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
            }
        }
        
        // Place the pivot in its correct sorted position
        int temp = nums[high];
        nums[high] = nums[i + 1];
        nums[i + 1] = temp;
        
        // After sorting or identifying the extremes, compute the product difference
        // For a full quicksort, you would recursively call quicksort on left and right sub-arrays.
        // Using direct array sorting for this specific problem:
        java.util.Arrays.sort(nums);
        return (nums[n - 1] * nums[n - 2]) - (nums[0] * nums[1]);
    }
}