class Solution {
    public int longestPalindrome(String s) {
        int len = s.length();
        
        if (len == 1)
            return 1;
        
        HashMap<Character, Integer> hash = new HashMap<Character, Integer>();
        
        for (char c : s.toCharArray()) {
            if (!hash.containsKey(c))
                hash.put(c, 1);
            else
                hash.put(c, hash.get(c) + 1);
        }
        
        int ans = 0, odd = 0;
        
        for (Map.Entry<Character, Integer> entry : hash.entrySet()) {
            int val = entry.getValue();
            
            if (val % 2 == 0)
                ans += val;
            else {
                ans += val - 1; 
                odd = 1;
            }
        }
        
        return ans + odd;
    }
}