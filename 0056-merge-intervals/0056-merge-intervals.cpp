class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ans;
        ans.push_back(intervals[0]);
            
        int end = ans[0][1];
        int idx = 0;
    
        for(int i = 1; i < n; i++) {
            int start = intervals[i][0];
            if(end >= start) {
                ans[idx][1] = max(intervals[i][1], end);
                end = ans[idx][1];
            } else {
                ans.push_back(intervals[i]);  
                end = intervals[i][1];
                ++idx;
            }
        }
        
        return ans;
    }
};