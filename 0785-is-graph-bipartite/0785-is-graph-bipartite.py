class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, m = len(graph), len(graph[0])
        adj = {i: [] for i in range(n)}
        arr = [-1] * n

        for i in range(n):
            for neighbor in graph[i]:
                adj[i].append(neighbor)

        for i in range(n):
            if arr[i] == -1:
                if self.bfs(i, adj, arr) == False:
                    return False
        return True

    def bfs(self, start, adj, arr) -> bool:
        deq = collections.deque()

        arr[start] = 1
        deq.append(start)

        while deq:
            node = deq.popleft()
            for nei in adj[node]:
                if arr[nei] != -1:
                    if arr[nei] == arr[node]:
                        return False
                    continue
                elif arr[node] == 1:
                    arr[nei] = 2
                elif arr[node] == 2:
                    arr[nei] = 1
                deq.append(nei)
        return True