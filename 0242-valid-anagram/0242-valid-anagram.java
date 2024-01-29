class Solution {
    public boolean isAnagram(String s, String t) {
      HashMap<Character, Integer> hash = new HashMap<Character, Integer>();
      
      int len_t = t.length();
      int len_s = s.length();
      
      if (len_t != len_s) 
        return false;
      
      for (int i = 0; i < len_t; i++) {
        char char_t = t.charAt(i);
        
        if (!hash.containsKey(char_t))
           hash.put(char_t, 1);
        else
            hash.put(char_t, 1 + hash.get(char_t));
      }
   
      for (int i = 0; i < len_s; i++) {
        char char_s = s.charAt(i);

        if (!hash.containsKey(char_s))
          return false;
        else
          hash.put(char_s, hash.get(char_s) - 1);
      }
      
      for (Map.Entry<Character, Integer> entry : hash.entrySet()) {
        if (entry.getValue() != 0)
          return false;
      }
      
      return true;
      
    }
}