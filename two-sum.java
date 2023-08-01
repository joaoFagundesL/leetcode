class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();

        int[] a = new int[2];

        for(int i = 0; i < nums.length; i++) {
            int aux = target - nums[i];
            if(!hash.containsKey(aux)) 
                hash.put(nums[i], i);
            else {
                a[0] = hash.get(aux);
                a[1] = i;
            }
        }
        return a;
    }
}
