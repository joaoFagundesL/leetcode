class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
      int numRows = image.length, numCols = image[0].length, color_start = image[sr][sc];
      
      if (numRows == 0)
        return image;
      
      int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
      boolean[][] visited = new boolean[numRows][numCols];
    
      
      Queue<String> queue = new LinkedList<>();
      queue.add(sr + "," + sc);
      
      while(!queue.isEmpty()) {
        String x = queue.remove();
        
        int row = Integer.parseInt(x.split(",")[0]);
        int col = Integer.parseInt(x.split(",")[1]);
        
        if (row < 0 || col < 0 || row >= numRows || col >= numCols || 
            visited[row][col] || image[row][col] != color_start) {
          continue;
        }
        
        image[row][col] = color;
        visited[row][col] = true;
        queue.add(row + "," + (col - 1)); //left
        queue.add(row + "," + (col + 1)); //right
        queue.add((row - 1) + "," + col); //up
        queue.add((row + 1) + "," + col); //down          
      }
      
      return image;
      
    }
}