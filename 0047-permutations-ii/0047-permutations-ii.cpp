class Solution {
public:
    void backtracking(set<vector<int>>& ans, int freq[], vector<int>& p, vector<int>& nums, int n) {
      
      if(p.size() == n) {
        ans.insert(p);
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
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
      int n = nums.size();
      int freq[n];
      for(int i = 0; i < n; i++)
        freq[i] = 0;
      
      set<vector<int>> ans;
      vector<int> p;
      
      backtracking(ans, freq, p, nums, n);
      
      vector<vector<int>> a;
      for(const auto &it : ans) {
        a.push_back(it);
      }
      
      return a;
     }
};