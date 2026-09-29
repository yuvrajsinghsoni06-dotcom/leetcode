class Solution {
    public int arrangeCoins(int n) {
        int result = n;
        int i;
        for(i = 1; result >= i;i++){
            if(result > 0){
                result -= i;
            }else{
                break;
            }
            
        }
        return i -1;
        
    }
}