class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
      HashMap<Character, Integer> hash = new HashMap<Character, Integer>();
      
      int len_ransom = ransomNote.length(), len_magazine = magazine.length();
      
      for (int i = 0; i < len_ransom; i++) {
        char charRansomNote = ransomNote.charAt(i);
        
        if (!hash.containsKey(charRansomNote))
          hash.put(charRansomNote, 1);
        else
          hash.put(charRansomNote, hash.get(charRansomNote) + 1);
      }
      
      for (int i = 0; i < len_magazine; i++) {
        char charMagazine = magazine.charAt(i);
        
        if (hash.containsKey(charMagazine))
          hash.put(charMagazine, hash.get(charMagazine) - 1);
        
      }
      
      for (Map.Entry<Character, Integer> entry : hash.entrySet()) {
        if (entry.getValue() > 0)
          return false;
      }
      
      return true;
    }
}