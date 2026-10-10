class Solution {
    public int maxProduct(int[] nums) {
        int max = nums[0];
        int mini = nums[0];
        int res = nums[0];

        for(int i =1;i<nums.length;i++){
            int curr = nums[i];

            if(curr < 0){
                int temp = max;
                max = mini;
                mini = temp;
            }
            max = Math.max(curr,max*curr);
            mini = Math.min(curr, mini*curr);
            res = Math.max(res,max);

        }
        return res;
    }
}