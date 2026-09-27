from collections import defaultdict
class MyHashSet:
 
    def __init__(self):
        self.hashset = defaultdict(int)
        

    def add(self, key: int) -> None:
        if self.hashset[key] == 0:
            self.hashset[key] = 1
        

    def remove(self, key: int) -> None:
        if self.hashset[key] == 1:
            self.hashset[key] = 0
        

    def contains(self, key: int) -> bool:
        return key in self.hashset and self.hashset[key] == 1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)