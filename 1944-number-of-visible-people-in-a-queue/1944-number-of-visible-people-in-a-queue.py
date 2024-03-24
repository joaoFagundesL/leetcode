class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        
        stack = deque()
        stack.append(heights[n - 1])
        n -= 2
        for i in range(n, -1, -1):
            v = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                v += 1
                
            ans[i] = v
            if stack: ans[i] += 1
                
            stack.append(heights[i])
        
        return ans
    
            