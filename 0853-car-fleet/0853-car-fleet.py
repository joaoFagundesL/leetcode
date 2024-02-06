class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        curr, ans, stack, = 0, 0, []
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        for p, s in arr:
            time = (target - p) / s # it needs to be float
            if curr < time:
                ans += 1
                curr = time
                
        return ans
        