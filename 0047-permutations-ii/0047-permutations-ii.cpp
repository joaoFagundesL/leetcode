class Solution {
public:
    void backtracking(vector<vector<int>>& ans, int freq[], vector<int>& p, vector<int>& nums, int n) {
      
      if(p.size() == n) {
        ans.push_back(p);
        return;
      }
      
      for(int i = 0; i < n; i++) {
        // freq[i - 1] = 0 means that i have already used, then i can safely skip it
        // freq[i] == 1 means that vector p already has this value
        
        // basically: check if the curr element is equal to its previous and if
        // one of them has already been used
        if(freq[i] == 1 || (i > 0 && nums[i] == nums[i - 1] && freq[i - 1] == 0))
          continue;
        freq[i] = 1;
        p.push_back(nums[i]);
        backtracking(ans, freq, p, nums, n);
        freq[i] = 0;
        p.pop_back(); 
      }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
      sort(nums.begin(), nums.end());
      int n = nums.size();
      int freq[n];
      for(int i = 0; i < n; i++)
        freq[i] = 0;
      
      vector<vector<int>> ans;
      vector<int> p;
      backtracking(ans, freq, p, nums, n);
      
      return ans;
     }
};