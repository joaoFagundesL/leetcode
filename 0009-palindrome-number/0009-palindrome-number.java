class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0, aux = x, ld = 0;
        
        if (x < 0) return false;
        
        while (aux != 0) {
            ld = aux % 10;
            rev = rev * 10 + ld;
            aux = aux / 10; 
        }
                
        while (x != 0) {
            x /= 10; rev /= 10;
            
            if (x != rev)
                return false;
        }
        
        return true;
    }
}