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
                print("added to heap: ", h)
                heapq.heappush(max_heap, h)
                
                if -max_heap[0] > max_height:
                    ans.append([x, -h])
                    max_height = -max_heap[0]
                    print("updated max height: ", max_height)
            else:
                
                if h in removed:
                    removed[h] += 1   
                    print("incremented to", removed[h], h)
                else:
                    print("first time inserted: ", h)
                    removed[h] = 1
                               
                while -max_heap[0] in removed and removed[-max_heap[0]] > 0:
                    print("-max_heap[0] is in removed", -max_heap[0])
                    print("removing 1 from", -max_heap[0])
                    
                    removed[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
                   
                if -max_heap[0] != max_height:
                    print("new high height", -max_heap[0])
                    ans.append([x, -max_heap[0]])
                    max_height = -max_heap[0]
                
                # print("AFTER")
                # print("removed ", removed)
                # print("heap ", max_heap)
                # print("\n")
                    
        return ans