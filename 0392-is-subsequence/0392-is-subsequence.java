class Solution {
    public boolean isSubsequence(String s, String t) {
       int k = 0, len = t.length(), len_s = s.length();
        
        if (len_s > len) return false;
        
        if (len_s == 0) return true;
        
        for (int i = 0; i < len; i++) {            
            char t_char = t.charAt(i); 
            char s_char = s.charAt(k);
            
            if (t_char == s_char) {
                System.out.println("t_char = " + t_char + " s_char = " + s_char);
                ++k;
            }
            
            if (k >= len_s) return true;
                
            
        }
        return false;
        
    }
}