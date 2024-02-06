class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highest_time, removed = -1, 0
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        for p, s in arr:
            time = (target - p)/s # it needs to be float
            if time <= highest_time:
                removed += 1
            else:
                highest_time = time
             
        return len(arr)-removed
        