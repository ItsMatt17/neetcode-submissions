class Node: 

    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.next = self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.map = {}
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def push(self, node): 
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = self.tail.prev = node

    def remove(self, node):    
        l, r = node.prev, node.next
        l.next, r.prev = r, l


    def get(self, key: int) -> int:
        if (key not in self.map): return -1
        node = self.map[key]

        self.remove(node)
        self.push(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if (key in self.map): 
            node = self.map[key]
            node.val = value

            self.remove(node)
            self.push(node)
            return
        
        
        if (self.size == self.cap):   
            node = self.map[self.head.next.key]
            self.remove(node)
            del self.map[node.key]
            self.size -= 1
        
        node = Node(key, value)
        self.map[key] = node

        self.push(node)
        self.size += 1







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)