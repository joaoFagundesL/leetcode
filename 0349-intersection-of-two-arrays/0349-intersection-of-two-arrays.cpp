class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> freq;
        
        for(const auto &e : nums1) {
            freq[e]++;
        }
        
        vector<int> ans;
        for(const auto &e : nums2) {
            auto x = freq.find(e);
            if(x != freq.end()) {
                ans.push_back(e);
                // to avoid duplicates
                freq.erase(x);
            }
        }
        
        return ans;
    }
};