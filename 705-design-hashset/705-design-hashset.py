class MyHashSet:

    def __init__(self):
        self.hash=[0 for i in range(10**6+1)]
        
    def add(self, key: int) -> None:
        if key<len(self.hash):
            self.hash[key]=1
        else:
            print(len(self.hash)==key)

    def remove(self, key: int) -> None:
        self.hash[key]=0

    def contains(self, key: int) -> bool:
        return self.hash[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)