class Solution:
    def __init__(self):
        self.deq = collections.deque()
        self.num_row = 0
        self.num_col = 0
        self.directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.num_row = len(mat)
        self.num_col = len(mat[0])
        ans = [[float('inf')] * self.num_col for _ in range(self.num_row)]
        
        for r in range(self.num_row):
            for c in range(self.num_col):
                if mat[r][c] == 0: # bfs from the zero
                    ans[r][c] = 0
                    self.deq.append((r, c))
                    
        while self.deq:  
            row, col = self.deq.popleft()
            for dr, dc in self.directions:
                newRow = row + dr
                newCol = col + dc
                        
                if (newRow < 0 or newCol < 0) or (newRow >= self.num_row or newCol >= self.num_col) or mat[newRow][newCol] == 0:
                    continue
                    
                if ans[newRow][newCol] > ans[row][col] + 1:
                    ans[newRow][newCol] = ans[row][col] + 1
                    self.deq.append((newRow, newCol))
                
        return ans
               