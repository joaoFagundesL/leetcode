class RandomizedSet:

    def __init__(self):
        self.my_hash = {}
        self.my_list = []

    def insert(self, val: int) -> bool:
        if val not in self.my_hash:
            self.my_hash[val] = len(self.my_list)
            self.my_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.my_hash:
            idx = self.my_hash[val]
            lastVal = self.my_list[-1]
            self.my_list[idx] = lastVal
            self.my_list.pop()
            self.my_hash[lastVal] = idx # update the new index of the element that was swapped
            del self.my_hash[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.my_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()