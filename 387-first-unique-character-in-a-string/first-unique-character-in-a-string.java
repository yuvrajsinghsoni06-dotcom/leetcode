class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> coll = new HashMap<>();

        for (char ch : s.toCharArray()) {
            coll.put(ch, coll.getOrDefault(ch, 0) + 1);
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (coll.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        
        return -1;
    }
}