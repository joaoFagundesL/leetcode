class Solution:
    def __init__(self):
        self.visited = set()
        self.deq = collections.deque()
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 1:
            return 1
        
        groups = 0
        for i in range(n):
            if strs[i] in self.visited:
                continue
            self.bfs(strs[i], strs, n)
            groups += 1
        
        return groups
    
    def bfs(self, curr_strs, strs, n):
        self.deq.append(curr_strs)
        self.visited.add(curr_strs)
        
        while self.deq:
            w = self.deq.popleft()
            for j in range(n):
                if strs[j] in self.visited:
                    continue
                if self.checkSimilar(strs[j], w):
                    self.deq.append(strs[j])
                    self.visited.add(strs[j])
                        
    def checkSimilar(self, w1, w2):
        matches = 0
        n = len(w1)
        for i in range(n):
            if w1[i] == w2[i]:
                matches += 1
        return n - matches <= 2
            
        
 