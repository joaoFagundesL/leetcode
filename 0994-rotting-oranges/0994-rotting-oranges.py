class Solution:
    def __init__(self):
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.deq = collections.deque()
        self.num_row = 0
        self.num_col = 0
        self.visited = set()
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.num_row, self.num_col = len(grid), len(grid[0])
        ans, fresh = 0, 0
        
        for i in range(self.num_row):
            for j in range(self.num_col):
                if grid[i][j] == 2:
                    self.deq.append((i, j, 0))
                    self.visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                
        while self.deq:
            row, col, time = self.deq.popleft()
            ans = max(ans, time)
            for dr, dc in self.directions:
                newRow, newCol = row + dr, col + dc
                
                if (
                    (newRow < 0 or newRow >= self.num_row) 
                    or (newCol < 0 or newCol >= self.num_col)
                    or (newRow, newCol) in self.visited 
                    or grid[newRow][newCol] == 0
                ): continue
                
                fresh -= 1
                grid[newRow][newCol] = 2
                self.deq.append((newRow, newCol, time + 1))
                self.visited.add((newRow, newCol))
        
        return -1 if fresh > 0 else ans
                
                
            