class Solution:
    def findWords(self, words: List[str]) -> List[str]:        
        h = {
            1: ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            2: ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            3: ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        }
        
        key = 0
        ans = []
        for word in words:
            if word[0].lower() in h[1]: key = 1
            elif word[0].lower() in h[2]: key = 2
            else: key = 3
            is_valid = True
            for char in word[1:]:
                if char.lower() not in h[key]:
                    is_valid = False
                    break
            if is_valid:
                ans.append(word)
        return ans