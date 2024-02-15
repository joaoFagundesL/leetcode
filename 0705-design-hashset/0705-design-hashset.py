class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(1000)]
        
    def add(self, key: int) -> None:
        bucketIdx = key % 1000
        if key not in self.buckets[bucketIdx]:
            self.buckets[bucketIdx].append(key)
            return True
        return False
    
    def remove(self, key: int) -> None:
        bucketIdx = key % 1000
        if key in self.buckets[bucketIdx]:
            self.buckets[bucketIdx].remove(key)
            return True
        return False
            
    def contains(self, key: int) -> bool:
        bucketIdx = key % 1000
        if key in self.buckets[bucketIdx]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)