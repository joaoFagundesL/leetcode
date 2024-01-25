class Solution {
    public String longestCommonPrefix(String[] strs) {
      return divideConquer(strs, 0, strs.length - 1);    
    }
    
  public String divideConquer(String[] strs, int start, int end) {
    if (start == end)
      return strs[start];
    
    int mid = start + ((end - start) / 2);
    
    String l_arr = divideConquer(strs, start, mid);
    String r_arr = divideConquer(strs, ++mid, end);
    
    return getPrefix(l_arr, r_arr);
  }
  
  public String getPrefix(String l_arr, String r_arr) {
    int len = Math.min(l_arr.length(), r_arr.length());
    
    for (int i = 0; i < len; i++) {
      if (l_arr.charAt(i) != r_arr.charAt(i)) {
          return l_arr.substring(0, i);
      }
    }
    
    return l_arr.substring(0, len);
  }
}