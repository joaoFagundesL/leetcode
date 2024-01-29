class Solution {
    public int[] productExceptSelf(int[] nums) {
      
      int len = nums.length, aux = 1;
      
      int ans[] = new int[len];
      ans[0] = 1;
                
      
      // left
      for (int i = 0; i < len - 1; i++) {
        aux *= nums[i];
        ans[i + 1] = aux; 
      }  
      
      len = len - 1;
      aux = 1;
      
      // right
      for (int i = len; i >= 1; i--) {
        aux *= nums[i];
        ans[i - 1] = aux * ans[i - 1];
      }
      
      return ans;
      
    }
}