class Solution {
    public int longestConsecutive(int[] nums) {
      
      HashSet<Integer> hash = new HashSet<Integer>();   
      
      int len = nums.length;
      
      for (int i = 0; i < len; i++) 
        hash.add(nums[i]);
      
      int curr = 0, max = 0, next;
      
      for (Integer e : hash) {
        int curr_element = e;
                
        if (!hash.contains(--curr_element)) {
          ++curr;
          
          next = curr_element + 2;
          
          while (hash.contains(next)) {
            ++curr;
            ++next;
          }
        }
        
        if (curr > max)
          max = curr;
        
        curr = 0;
        
      }
      
      return max;
    }
}