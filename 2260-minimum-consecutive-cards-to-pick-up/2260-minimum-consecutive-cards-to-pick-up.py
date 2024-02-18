class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        h, start, end, len_cards, ans = set(), 0, 0, len(cards), float('inf')
        
        while end < len_cards:
          while cards[end] in h:
            ans = min(ans, end - start + 1)
            h.remove(cards[start])
            start += 1
            
          if cards[end] not in h:
            h.add(cards[end])
          end += 1
  
        if ans == float('inf'): return -1
        else: return ans