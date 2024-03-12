class Solution {
public:
    void backtracking(vector<vector<int>>& ans, int freq[], vector<int>& p, vector<int>& nums, int n) {
      
      if(p.size() == n) {
        ans.push_back(p);
        return;
      }
      
      for(int i = 0; i < nums.size(); i++) {
        if(freq[i] == 1)
          continue;
        
        freq[i] = 1;
        p.push_back(nums[i]);
        backtracking(ans, freq, p, nums, n);
        freq[i] = 0;
        p.pop_back();
      }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
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