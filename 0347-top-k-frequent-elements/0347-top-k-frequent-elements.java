class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hash = new HashMap<>();
            
        int len = nums.length;
        
        for(int i = 0; i < len; i++) {
            if(!hash.containsKey(nums[i]))
                hash.put(nums[i], 1);
            else
                hash.put(nums[i], 1 + hash.get(nums[i]));
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> maxPQ =  
                             new PriorityQueue<>((a, b) -> b.getValue() - a.getValue()); 
                  
        
        for(Map.Entry<Integer, Integer> entry : hash.entrySet()) 
            maxPQ.add(entry);
        
        
        int[] ans = new int[k];
        
        for (int i = 0; i < k; i++) 
            ans[i] = maxPQ.poll().getKey();

        
        return ans;
        

    }
}