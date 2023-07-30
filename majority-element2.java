class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();

        int len = nums.length;
        for(int i = 0; i < len; i++) {
            if(hash.containsKey(nums[i]))
                hash.put(nums[i], hash.get(nums[i]) + 1);
            else
                hash.put(nums[i], 1);
        }

        List<Integer> list = new ArrayList<>();

        len /= 3;

        for(Map.Entry<Integer, Integer> entry : hash.entrySet()) {
            if(entry.getValue() > len)                 
                list.add(entry.getKey());
        }

        return list;
    }
}
