class Solution:
    def repeatedCharacter(self, s: str) -> str:
        h = set()
        
        for c in s:
            if c not in h:
                h.add(c)
            else:
                return c
        
        
        