class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
      int numRows = image.length, numCols = image[0].length, color_start = image[sr][sc];
      
      if (numRows == 0)
        return image;
      
      // {x, y} => {row, col} => {move left} {move right} {move up} {move down}
      int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
      boolean[][] visited = new boolean[numRows][numCols];
    
      Queue<int[]> queue = new LinkedList<>();
      
      // add the starting point to initiate the BFS
      queue.add(new int[]{sr, sc});
      visited[sr][sc] = true;
      image[sr][sc] = color; 
    
      while(!queue.isEmpty()) {
        int[] curr = queue.remove();
        
        int row = curr[0];
        int col = curr[1];
         
        // add all neighbors in the queue
        for (int[] direction : directions) {
          int newRow = row + direction[0]; // => {-1, 0}, {1, 0}
          int newCol = col + direction[1]; // => {0, -1}, {0, 1}
                   
          if (newRow < 0 || newCol < 0 || newRow >= numRows || newCol >= numCols || 
              visited[newRow][newCol] || image[newRow][newCol] != color_start) {
            continue;
          }

          image[newRow][newCol] = color;
          visited[newRow][newCol] = true;
          queue.add(new int[]{newRow, newCol});
        }
      }
      
      return image;
      
    }
}