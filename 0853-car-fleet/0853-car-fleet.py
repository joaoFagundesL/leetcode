class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highest_speed, removed = -1, 0
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        for p, s in arr:
            time = (target - p)/s # it needs to be float
            if time <= highest_speed:
                removed += 1
            highest_speed = max(highest_speed,time)
             
        return len(arr)-removed
        