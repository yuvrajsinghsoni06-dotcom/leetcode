class Solution {
    public int maximumWealth(int[][] accounts) {
        int res = 0, amount = 0;
        int m = accounts.length;
        int n = accounts[0].length;
        for(int i= 0; i < m; i++){
            amount = 0;
            for(int j = 0; j< n;j++){
                amount += accounts[i][j];
            }
            res = Math.max(res,amount);
        }
        return res;
        
    }
}