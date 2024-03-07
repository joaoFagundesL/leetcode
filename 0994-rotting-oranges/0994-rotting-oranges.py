class Solution:        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        deq = collections.deque()
        visited = set()
        num_row, num_col = len(grid), len(grid[0])
        ans, fresh = 0, 0
        
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == 2:
                    deq.append((i, j, 0))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                
        while deq:
            row, col, time = deq.popleft()
            ans = max(ans, time)
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                
                if (
                    (newRow < 0 or newRow >= num_row) 
                    or (newCol < 0 or newCol >= num_col)
                    or (newRow, newCol) in visited 
                    or grid[newRow][newCol] == 0
                ): continue
                
                fresh -= 1
                grid[newRow][newCol] = 2
                deq.append((newRow, newCol, time + 1))
                visited.add((newRow, newCol))
                
        return -1 if fresh > 0 else ans
                
                
            