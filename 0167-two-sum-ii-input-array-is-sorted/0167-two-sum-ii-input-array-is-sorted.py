class Solution(object):
    def twoSum(self, numbers, target):
        x, y = 0, len(numbers) - 1
        
        while x < y:
            total = numbers[x] + numbers[y]
            
            if total < target:
                x += 1
            elif total > target:
                y -= 1
            else:
                x += 1
                y += 1
                return [x, y]
        
        return -1
        