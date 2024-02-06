class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        removed = 0
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        
        highest_time = (target-arr[0][0])/arr[0][1]
        
        for p, s in arr[1:]:
            time = (target - p)/s # it needs to be float
            if time <= highest_time:
                removed += 1
            else:
                highest_time = time
             
        return len(arr)-removed
        