/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
      int l = 1, r = n, ans = r;
      
      while (l <= r) {
        int myGuess = ((r - l) /2 ) + l;
        
        if (isBadVersion(myGuess)) {
          ans = Math.min(myGuess, ans);
          r = myGuess - 1;
        }
        
        else {
          l = myGuess + 1;
        }
      }
      
      return ans;
    }
}