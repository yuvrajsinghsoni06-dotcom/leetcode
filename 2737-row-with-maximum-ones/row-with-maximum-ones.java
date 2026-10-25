class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int r = mat.length;
        int c = mat[0].length;
        int bestidx = 0,count = 0;

        for(int i = 0;i<r;i++){
            int freq = 0;
            for(int j = 0;j<c;j++){
                if(mat[i][j] == 1){
                    freq++;
                }
            }
            if(freq > count){
                count = freq;
                bestidx = i;
            }
        }
        return new int[] {bestidx,count};
        
    }
}