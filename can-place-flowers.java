class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        int len = flowerbed.length;

        /* If the size is 5, for example, i can plant 5/2 plots. But i have to round up, so 
        i get the even number after that (6), because 6/2 is 3
        
        [1, 0, 1, 0, 1] 

        */
        if(len % 2 != 0) 
            len++;

        int possible = len / 2;
        int planted = 0;

        for(int i = 0; i < flowerbed.length; i++) {
            if(flowerbed[i] == 1)
                planted++;
        }

        if( n > (possible - planted))
            return false;
        else
            return true;
    }
}
