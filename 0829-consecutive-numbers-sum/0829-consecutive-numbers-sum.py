class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        staircase = 1
        w = 1
        count = 0
        
        while staircase <= n:
            block = n - staircase
            h = block // w
            
            # total area
            if w * h + staircase == n:
                count += 1
            w += 1
            # if i want the sum in the range of [5,7] then width is 3
            # [3, 4] width is 2
            # it's only possible to visualize this drawing
            # basically 1 + 2 + 3 ... + width
            staircase += w
        return count

