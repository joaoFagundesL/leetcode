class Solution {
  public int minEatingSpeed(int[] piles, int h) {
    int len = piles.length, max = Integer.MIN_VALUE;
    
    for (int i = 0; i < len; i++) {
      if (piles[i] > max)
        max = piles[i];
    }
    
    int r = max, ans = r, l = 1;
    
    while(l <= r) {
      int m = ((r - l) / 2) + l;
      
      if (check(piles, m, len) <= h) { // it means koko ate too fast
        // a value can sastify the hours but it may not be the solution because there's a smaller value
        ans = Math.min(m, ans); 
        r = m - 1 ;    
      } else
         l = m + 1;
    }
    
    return (int) ans;
  }
  
  public int check(int[] piles, int m, int len) {
    int sum = 0;
    
    for (int i = 0; i < len; i++) 
      sum += Math.ceil((double) piles[i] / m);
    
    return sum;
  }
}