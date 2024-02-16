class Solution:
    def __init__(self):
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.deq = collections.deque()

        self.visited = set()
        self.num_row = 0
        self.num_col = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.num_row = len(grid)
        self.num_col = len(grid[0])
        
        island = 0
        # go one by one but just apply bfs if it is not visited and if it is a 1
        for r in range(self.num_row):
            for c in range(self.num_col):
                if (r, c) not in self.visited and grid[r][c] == "1":
                    # will get all connected 1's excluding 0 from the queue
                    self.bfs(grid, r, c) 
                    island += 1
        return island

        
    def bfs(self, grid: List[List[str]], r: int, c: int) -> int:
        
        # it's inside the range, so is safe to add
        self.visited.add((r, c))
        self.deq.append((r, c))
                
        # get every valid neighbor 
        while self.deq:
            row, col = self.deq.popleft()
            # loop 4-directions
            for dr, dc in self.directions:
                newRow = row + dr
                newCol = col + dc
                
                # only add to the deq if it is valid
                if (newCol < 0 or newRow < 0) or (newCol >= self.num_col or newRow >= self.num_row) or ((newRow, newCol) in self.visited) or (grid[newRow][newCol] != "1"):
                    continue
                
                # safe to add everything
                self.visited.add((newRow, newCol))
                self.deq.append((newRow, newCol))