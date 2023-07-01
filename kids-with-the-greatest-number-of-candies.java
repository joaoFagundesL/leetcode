class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        List<Boolean> list = new ArrayList<>();
        int max = 0;

        for(int i = 0; i < candies.length; i++) {
            if(candies[i] > max)
                max = candies[i];
        }

        int necessary = max - extraCandies;

        for(int i = 0; i < candies.length; i++) {
            if(candies[i] < necessary)
                list.add(false);
            else 
                list.add(true);
        }
        
        return list;
    }
}
