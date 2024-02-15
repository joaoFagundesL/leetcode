class RandomizedSet:
    def __init__(self):
        self.buckets = [[] for _ in range(16)] 
        self.filled_buckets = {}
        
    def insert(self, val: int) -> bool:
        bucketIdx = val % 16
        if val not in self.buckets[bucketIdx]:
            self.buckets[bucketIdx].append(val)
            self.filled_buckets[val] = self.filled_buckets.get(val, 0) + 1
            return True
        else: 
            return False
        
    def remove(self, val: int) -> bool:
        bucketIdx = val % 16
        if val in self.buckets[bucketIdx]:
            self.buckets[bucketIdx].remove(val)
            if val in self.filled_buckets:
                self.filled_buckets[val] -= 1
                if self.filled_buckets[val] == 0:
                    del self.filled_buckets[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.filled_buckets.keys()))
       