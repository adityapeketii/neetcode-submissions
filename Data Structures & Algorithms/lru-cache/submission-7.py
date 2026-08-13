class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

    # insert node at right  
    def insert(self, node):
        prev, nst = self.right.prev, self.right
        prev.nxt, nst.prev = node, node
        node.prev = prev
        node.nxt = nst

    def remove(self, node):
        prev, nst = node.prev, node.nxt
        prev.nxt, nst.prev = nst, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # update the lru and mru
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove the lru
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

        
