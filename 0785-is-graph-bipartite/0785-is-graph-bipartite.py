class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, m = len(graph), len(graph[0])
        # -1 = not visited, 0 and 1 are the groups
        arr = [-1] * n
        
        # handling the case if not all vertex are reachable
        for i in range(n):
            if arr[i] == -1:
                if self.bfs(i, graph, arr) == False:
                    return False
        return True

    def bfs(self, start, adj, arr) -> bool:
        deq = collections.deque()

        arr[start] = 0
        deq.append(start)

        while deq:
            node = deq.popleft()
            for nei in adj[node]:
                if arr[nei] != -1: # visited
                    if arr[nei] == arr[node]: # same group
                        return False
                    continue
                # setting valid groups for unvisited nodes
                if arr[node] == 1:
                    arr[nei] = arr[node] & 0
                else:
                    arr[nei] = arr[node] ^ 1
                deq.append(nei)
        return True