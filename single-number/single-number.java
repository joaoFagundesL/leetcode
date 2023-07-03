class Solution {
    public int singleNumber(int[] nums) {
        int len = nums.length;

        HashMap<Integer, Integer> hash = new HashMap<>();

        for(int i = 0; i < len; i++) {
            if(!hash.containsKey(nums[i]))
                hash.put(nums[i], 1);
            else 
                hash.put(nums[i], 1 + hash.get(nums[i]));
        }

        int key = 0;
        for(Map.Entry<Integer, Integer> entry : hash.entrySet()) {
            if(entry.getValue() == 1) {
                key = entry.getKey();
                break;
            }
        }

        return key;
    }
}
