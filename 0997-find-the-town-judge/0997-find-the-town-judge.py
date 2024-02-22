class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        h, count = {}, {}
        
        # adjacency list
        for v1, v2 in trust:
            if v1 not in h:
                h[v1] = [v2]
            else:
                h[v1].append(v2)
        
        # counting how many people trust in the other person
        for v1, v2 in trust:
            count[v2] = count.get(v2, 0) + 1
        
        for judge, t in count.items():
            if t == n - 1 and judge not in h:
                return judge
        return -1