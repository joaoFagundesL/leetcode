class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        int len = nums.length;

        for(int i = 0; i < len; i++) {
            if(hash.containsKey(nums[i])) {
                int value = hash.get(nums[i]) + 1;
                hash.put(nums[i], value);
            } else 
                hash.put(nums[i], 1);
            
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
