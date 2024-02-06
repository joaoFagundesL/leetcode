class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans, stack, = 1, []
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        for p, s in arr:
            stack.append((target - p) / s) # it needs to be float
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # -1 is the top of the stack
                stack.pop()
        return len(stack)
        