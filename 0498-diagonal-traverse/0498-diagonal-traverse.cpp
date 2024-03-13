class Solution {
public:
        vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
                map<int, vector<int>> hash;
                int n = mat.size(), m = mat[0].size();
                vector<int> ans;
                
                for(int i = 0; i < n; i++) {
                        for(int j = 0; j < m; j++) {
                                // the sum represents each diagonal
                                int idx = i + j;
                                hash[idx].push_back(mat[i][j]);

                        }
                }
                
                for(const auto &pair : hash) {
                        int len = pair.second.size();
                        // even number = go up
                        if(!(pair.first & 1)) {
                                for(int i = len - 1; i >= 0; i--) {
                                        ans.push_back(pair.second[i]);
                                }
                        } else {
                                for(int i = 0; i < len; i++) {
                                        ans.push_back(pair.second[i]);
                                }
                        }
                }

                return ans;
    }
};