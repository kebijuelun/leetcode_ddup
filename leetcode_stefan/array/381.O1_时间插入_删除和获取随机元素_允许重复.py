import random
import os
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = True
        if val in self.arr:
            flag = False
        self.arr.append(val)
        return flag
		

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        #flag = True
        if val not in self.arr:
            return False
        else:
            self.arr.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if len(self.arr) > 0:
            return random.choice(self.arr)
        else:
            return None


