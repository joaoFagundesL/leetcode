class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}

        for flight in flights:
            v1, v2, w = flight
            if v1 not in adj:
                adj[v1] = []
            adj[v1].append((v2, w))

            if v2 not in adj:
                adj[v2] = []
        heap = [(0, src, 0)]
        stops = [float('inf')] * n
        stops[src] = 0
        dist = [float('inf')] * n
        dist[src] = 0
        k = k + 1
        while heap:
            curr_weight, curr_node, curr_stops = heapq.heappop(heap)
            if curr_node == dst:
                return curr_weight
            if curr_stops >= k:
                continue
            print(curr_node)
            for next_node, next_weight in adj[curr_node]:
                total_weight = curr_weight + next_weight
                total_stops = curr_stops + 1
                
                if total_weight < dist[next_node] or total_stops <= stops[next_node]:
                    dist[next_node] = total_weight
                    stops[next_node] = total_stops
                    heapq.heappush(heap, (total_weight, next_node, total_stops))
        return -1    