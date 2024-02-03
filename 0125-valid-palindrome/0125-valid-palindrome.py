class Solution(object):
    def isPalindrome(self, s):
        s = s.lower() # convert to lower case
        pattern = r'[^A-Za-z0-9]' # match anything that is not alphanumeric
        new_string = re.sub(pattern, '', s) # replace for empty string
        
        start, end = 0, len(new_string) - 1
        
        while start <= end:
            if new_string[start] != new_string[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
        
        
        
        
        