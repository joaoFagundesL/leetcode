class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        c, r = len(word1), len(word2)
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        
        for i in range(r + 1): dp[i][0] = i
        for i in range(c + 1): dp[0][i] = i
            
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
        return dp[-1][-1]
    
    
    # ""  H   O  R   S   E
# ""  0   1   2  3   4   5
# R   1          X
# O   2
# S   3

# X => R == R in this case i want to transform HOR->R
# And if i fill the other positions i now that:
# HOR->''= 3
# HO->R = 2
# HO->"" = 2

# Since HOR->R R == R i dont need to do anything, so the case now is HO->R that is equal to 2
