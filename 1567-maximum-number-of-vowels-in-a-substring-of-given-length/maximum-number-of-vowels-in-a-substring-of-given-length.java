class Solution {
    private boolean isVowel(char ch){
        return ch=='a'|| ch=='e'|| ch=='i'|| ch=='o'||ch=='u';

    }
    public int maxVowels(String s, int k) {
        int res =Integer.MIN_VALUE;
        int c=0;
        int l=0,r=0;
        while(r<s.length()){
            if(isVowel(s.charAt(r))){
                c++;
            }
            if(r-l+1>k){
                if(isVowel(s.charAt(l))){
                    c--;
                }
                l++;
            }
            if(r-l+1==k){
                res=Math.max(res,c);
            }
            r++;

        }
        return res;

    }
}