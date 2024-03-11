class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
      int n = intervals.size();
      vector<vector<int>> ans;
      int i = 0;
      // no overlapping intervals
      while(i < n && intervals[i][1] < newInterval[0]) {
        ans.push_back(intervals[i++]);
      }
      
      // merge intervals
      while(i < n && newInterval[1] >= intervals[i][0]) {
        int mn = min(newInterval[0], intervals[i][0]);
        int mx = max(newInterval[1], intervals[i][1]);
        // set newInterval instead of adding directly to the ans
        newInterval[0] = mn;
        newInterval[1] = mx;
        ++i;
      }
      
      ans.push_back(newInterval);
      
      // insert remaining intervals
      while(i < n) {
        ans.push_back(intervals[i++]);
      }
      
      return ans; 
      
    }
};