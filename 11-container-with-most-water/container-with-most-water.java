class Solution {
    public int maxArea(int[] height) {
        int res = Integer.MIN_VALUE;
        int i = 0;
        int j = height.length - 1; // Fixed: start at the last valid index
        
        while (i < j) {
            int width = j - i;
            int h = Math.min(height[i], height[j]);
            int area = h * width;
            res = Math.max(area, res);
            
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        
        return res;
    }
}