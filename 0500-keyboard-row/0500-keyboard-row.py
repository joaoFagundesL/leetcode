#first solution (not very optimal)
# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:        
#         h = {
#             1: ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#             2: ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#             3: ['z', 'x', 'c', 'v', 'b', 'n', 'm']
#         }
        
#         key = 0
#         ans = []
#         for word in words:
#             if word[0].lower() in h[1]: key = 1
#             elif word[0].lower() in h[2]: key = 2
#             else: key = 3
#             is_valid = True
#             for char in word[1:]:
#                 if char.lower() not in h[key]:
#                     is_valid = False
#                     break
#             if is_valid:
#                 ans.append(word)
#         return ans

class Solution:
    def findWords(self, words: List[str]) -> List[str]:        
        h = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
            'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
            'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
        }
        
        key = 0
        ans = []
        for word in words:
            key = h[word[0].lower()]
            is_valid = True
            for char in word[1:]:
                if h[char.lower()] != key:
                    is_valid = False
                    break
            if is_valid:
                ans.append(word)
        return ans