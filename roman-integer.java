class Solution {

    public int romanToInt(String s) {
        HashMap<Character, Integer> algarisms = new HashMap<>();

        algarisms.put('I', 1);
        algarisms.put('V', 5);
        algarisms.put('X', 10);
        algarisms.put('L', 50);
        algarisms.put('C', 100);
        algarisms.put('D', 500);
        algarisms.put('M', 1000);

        int sum = 0;

        int len = s.length();

        for(int i = 0; i < len; i++) {
            char firstAlgarism = s.charAt(i);
            int firstValue = algarisms.get(firstAlgarism);

            if(i + 1 < len) {
                char secondAlgarism = s.charAt(i + 1);
                int secondValue = algarisms.get(secondAlgarism);

                if(firstValue >= secondValue) 
                    sum += firstValue;
                
                else {
                    sum += (secondValue - firstValue);
                    
                    /* Let's say for example I have "XIV", what i do is compare I < V. If is true,
                    then I make V - I. However the next loop there's no need to sum the V again,
                    that's why i make i++. In another words, im jumping the V.
                    */
                    i++; 
                }
            }

            /* The last one i can just add to the sum because there wont any element after it */
            else 
                sum += firstValue;
        }

        return sum;
    }
}

