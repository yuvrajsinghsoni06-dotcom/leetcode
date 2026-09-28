import java.util.HashSet;
import java.util.Arrays;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // Sort nums2 to enable binary search
        Arrays.sort(nums2);
        
        // Use a Set to store unique elements
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < nums1.length; i++) {
            int left = 0;
            int right = nums2.length - 1;
            
            while (left <= right) {
                int mid = left + (right - left) / 2;
                
                if (nums2[mid] == nums1[i]) {
                    set.add(nums1[i]);
                    break;
                } else if (nums1[i] < nums2[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        
        // Convert the Set back to an array
        int[] result = new int[set.size()];
        int idx = 0;
        for (int num : set) {
            result[idx++] = num;
        }
        
        return result;
    }
}