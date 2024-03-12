class Solution {
public:
    void backtracking(vector<vector<int>>& ans, int freq[], vector<int>& p, vector<int>& nums, int n, set<vector<int>>& hash) {
      
      if(p.size() == n && hash.find(p) == hash.end()) {
        ans.push_back(p);
        hash.insert(p);
        return;
      }
      
      for(int i = 0; i < nums.size(); i++) {
        if(freq[i] == 1) 
          continue;
        freq[i] = 1;
        p.push_back(nums[i]);
        backtracking(ans, freq, p, nums, n, hash);
        freq[i] = 0;
        p.pop_back(); 
        
      }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
      int n = nums.size();
      int freq[n];
      for(int i = 0; i < n; i++)
        freq[i] = 0;
      
      vector<vector<int>> ans;
      vector<int> p;
      set<vector<int>> hash;
      
      backtracking(ans, freq, p, nums, n, hash);
      
      
      return ans;
     }
};