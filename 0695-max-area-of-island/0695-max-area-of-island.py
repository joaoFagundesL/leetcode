class Solution:
    def __init__(self):
        self.deq = collections.deque()
        self.visited = set()
        self.num_row = 0
        self.num_col = 0
        self.directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.island_area = 1
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.num_row = len(grid)
        self.num_col = len(grid[0])
        
        max_area = 0
        island_area = 0
        for r in range(self.num_row):
            for c in range(self.num_col):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    self.island_area = 1 # reset area for the next island
                    self.bfs(grid, r, c)
                    max_area = max(max_area, self.island_area)

        return max_area
    
    def bfs(self, grid: List[List[int]], r: int, c: int) -> int:
        self.deq.append((r, c))
        self.visited.add((r, c))
        
        while self.deq:
            row, col = self.deq.popleft()
            for dr, dc in self.directions:
                newRow = row + dr
                newCol = col + dc
                if (newRow < 0 or newCol < 0) or (newRow >= self.num_row or newCol >= self.num_col) or ((newRow, newCol) in self.visited) or (grid[newRow][newCol] == 0):
                    continue
                self.deq.append((newRow, newCol))
                self.visited.add((newRow, newCol))
                self.island_area += 1 # calc area for the curr island

                
        