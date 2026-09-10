class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int r = 0;
        int l = 0;
        int sum = 0;
        int res = Integer.MAX_VALUE;

        while (r < nums.length) {
            sum += nums[r]; // Fixed: changed nums[i] to nums[r]
            
            while (sum >= target) { // Fixed: corrected 'whike' to 'while' (l <= r condition is redundant since sum >= target ensures l stays <= r for positive numbers)
                res = Math.min(res, r - l + 1); // Fixed: calculated minimum length BEFORE incrementing 'l'
                sum -= nums[l];
                l++;
            }
            r++;
        }

        return res == Integer.MAX_VALUE ? 0 : res; // Fixed: added missing return statement
    }
}