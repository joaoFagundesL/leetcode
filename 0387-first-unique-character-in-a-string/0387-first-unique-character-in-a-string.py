class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr, len_s = [0] * 26, len(s)
        
        for idx in range(len_s): 
            arr[ord(s[idx]) - ord('a')] += 1 # counting the frequency of each char in the corresponding position
            
        # get from the array the value of the first letter (it's not the first position of the array, hence the ascii calc)    
        for idx in range(len_s):
            if arr[ord(s[idx]) - ord('a')] == 1: 
                return idx
        return -1
            
            