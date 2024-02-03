class Solution(object):
    def getSkyline(self, buildings):
        arr, ans = [], []
        
        for building in buildings:
            arr.append([building[0], -building[2]]) # negative means start of building
            arr.append([building[1], building[2]])  # postive measn end of building
    
        arr.sort()
        
        max_height, max_heap = 0, []
        heapq.heappush(max_heap, 0)
                
        removed = {} 
        
        for building in arr:
            x, h = building[0], building[1]
            
            if h < 0:
                heapq.heappush(max_heap, h)
                
                if -max_heap[0] > max_height:
                    ans.append([x, -h])
                    max_height = -max_heap[0]
            else:
                removed[h] = removed.get(h, 0) + 1 # counting the frequency of the keys
                               
                while -max_heap[0] in removed and removed[-max_heap[0]] > 0:
                    removed[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
                   
                if -max_heap[0] != max_height:
                    ans.append([x, -max_heap[0]])
                    max_height = -max_heap[0]
                    
        return ans