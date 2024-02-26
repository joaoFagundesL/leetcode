class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        c, r = len(word1), len(word2)
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return (c - dp[r][c]) + (r - dp[r][c])