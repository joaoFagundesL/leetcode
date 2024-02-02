class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
      int numRows = image.length, numCols = image[0].length, color_start = image[sr][sc];
      
      if (numRows == 0)
        return image;
      
      int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
      boolean[][] visited = new boolean[numRows][numCols];
    
      
      Queue<int[]> queue = new LinkedList<>();
      queue.add(new int[]{sr, sc});
      
      while(!queue.isEmpty()) {
        int[] curr = queue.remove();
        
        int row = curr[0];
        int col = curr[1];
        
        if (row < 0 || col < 0 || row >= numRows || col >= numCols || 
            visited[row][col] || image[row][col] != color_start) {
          continue;
        }
        
        image[row][col] = color;
        visited[row][col] = true;
        
        for (int[] direction : directions) {
          int newRow = row + direction[0];
          int newCol = col + direction[1];
          queue.add(new int[]{newRow, newCol});
        }
      }
      
      return image;
      
    }
}