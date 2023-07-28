class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();

        int len = nums.length;

        for(int i = 0; i < len; i++) {
            if(hash.containsKey(nums[i])) 
                hash.put(nums[i], hash.get(nums[i]) + 1);
            else
                hash.put(nums[i], 1);
        }

        int result = 0;
        len /= 2;
        for(Map.Entry<Integer, Integer> entry : hash.entrySet()) {
            if(entry.getValue() > len) {
                result = entry.getKey();
                break;
            };
        }

        return result;
    }
}
