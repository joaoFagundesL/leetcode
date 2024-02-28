class Solution:
    def __init__(self):
        self.visited = set()
        self.deq = collections.deque()
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        
        province = 0
        # loop through the rows (rows is all the nodes and the col is the neighbours)
        for i in range(n):
            if i in self.visited or isConnected[i] == 0:
                continue
            province += 1
            self.bfs(i, isConnected)
        
        return province
                
    def bfs(self, c, isConnected):
        self.visited.add(c)
        self.deq.append(c)
        
        while self.deq:
            curr = self.deq.popleft()
            neighb = len(isConnected[curr])
            # now loop through the col that is neighbours
            for i in range(neighb):
                if isConnected[curr][i] == 0 or i in self.visited:
                    continue
                self.deq.append(i)
                self.visited.add(i)
                
            