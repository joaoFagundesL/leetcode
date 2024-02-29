class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        _in = [0] * n
        # out = [0] * n
        m = len(edges)
        
        for i in range(m):
          src = edges[i][0]
          dst = edges[i][1]
          _in[dst] += 1
          # out[src] += 1
        
        ans = []
        for i in range(n):
          if _in[i] == 0:
            ans.append(i)
        return ans