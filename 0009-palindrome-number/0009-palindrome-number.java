class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0, aux = x, ld = 0;
        
        if (x < 0) return false;
        
        while (aux != 0) {
            ld = aux % 10;
            rev = rev * 10 + ld;
            aux = aux / 10; 
        }
                
        return rev == x;
            }
}