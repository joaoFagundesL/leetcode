class Solution:    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
      num_row = len(mat)
      num_col = len(mat[0])
      ans = [[float('inf')] * num_col for _ in range(num_row)]
      directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
      deq = collections.deque()
      
      for r in range(num_row):
        for c in range(num_col):
          if mat[r][c] == 0: # bfs from the zero
            ans[r][c] = 0
            deq.append((r, c))

      while deq:  
        row, col = deq.popleft()
        for dr, dc in directions:
          newRow = row + dr
          newCol = col + dc

          if (newRow < 0 or newCol < 0) or (newRow >= num_row or newCol >= num_col) or mat[newRow][newCol] == 0:
            continue

          if ans[newRow][newCol] > ans[row][col] + 1:
            ans[newRow][newCol] = ans[row][col] + 1
            deq.append((newRow, newCol))

      return ans
