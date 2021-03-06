class MyHashSet:  # 58.65% 52.62%

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = set()

    def add(self, key: int) -> None:
        self.arr.add(key)

    def remove(self, key: int) -> None:
        self.arr.discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.arr:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
