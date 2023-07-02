class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.length;
        int max = 0;

        /*Assuming [0,0,0], the max i can place is [1,0,1]. What i did was take the size of the array
        and divide by two (fill all even positions). But if the array is odd, i can round up. In this example,
        3/2 is = 1, but i can place 2 elements. So i make (3+1)/2 = 2. This is valid for every odd size. The even ones
        is just divide by two because the even and odd index are the same in terms of quantity
        */

        /* This if..else is just to optimize as i wont need to go through the array later if it's false. */
        
        if(len % 2 != 0) 
            max = (flowerbed.length + 1) / 2;
        else 
            max = flowerbed.length / 2;

        if(n > max) 
            return false;


        /* There are two possibilites. Or i move three positions ahead or just two positions.
        For example: [1, 0, 0, 1]
                         ^------ Three positions ahed from here until i got another 1
        Or: [1, 0, 1]
                ^---- Two positions ahead from here until another 1               
         */

        int aux = 0;
        while(aux < flowerbed.length) {

            /* I'll move two ahead, but the third one can be a 1 */
            if(flowerbed[aux] == 1) {
                aux += 2;

            /* I have to check if the next one is 1, because as i mention there is 2 possibilites. 
             [1, 0, 0, 1, 0, 0]
                    ^------I'm here
            */

            } else if(aux + 1 < flowerbed.length && flowerbed[aux + 1] == 1) {
                /* [1, 0, 0, 1, 0, 0] 
                             ^---- I'm here now

                    [1, 0, 0, 1, 0, 0]
                                    ^-- Afterward, when I return  back to the first {if} I'll be here
                */                  
                aux++;

            } else {
                /* [1, 0, 0, 1, 0, 1]  => new array */
                flowerbed[aux] = 1;
                n--;
            }
            
        }

        return n <= 0;
    }
}
