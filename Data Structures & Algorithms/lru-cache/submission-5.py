class Doubly_LL:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key, self.val, self.next, self.prev = key, val, next, prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity, self.lru_cache, self.head, self.tail = capacity, {}, None, None

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            node_accesed = self.lru_cache[key]
            print(f"Node to return Key {node_accesed.key}, Value: {node_accesed.val}")
            if len(self.lru_cache) > 1:
                self.remove_dll_node(node_accesed)
                self.insert_node_at_end(node_accesed)
            return node_accesed.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print(f"lru_cache before Put: {[self.lru_cache[key].key for key in self.lru_cache.keys()]}")
        if key in self.lru_cache:
            node_accesed = self.lru_cache[key]
            node_accesed.val = value
            if len(self.lru_cache) > 1 and node_accesed != self.tail:
                self.remove_dll_node(node_accesed)
                self.insert_node_at_end(node_accesed)
        else:
            nodeToUpdate = Doubly_LL(key, value)

            if len(self.lru_cache) == 0:
                self.head = self.tail = nodeToUpdate
                self.lru_cache[key] = nodeToUpdate
            else:   
                self.insert_node_at_end(nodeToUpdate) 
                self.lru_cache[key] = nodeToUpdate
                if len(self.lru_cache) > self.capacity:
                    del self.lru_cache[self.head.key]
                    self.remove_dll_node(self.head)

        print(f"lru_cache after Put: {[self.lru_cache[key].key for key in self.lru_cache.keys()]}")

    def remove_dll_node(self, dll_node):
        print(f"Node to be removed Key: {dll_node.key}, Value: {dll_node.val}")
        if dll_node == self.head:
            self.head, dll_node.next.prev = dll_node.next, None
        elif dll_node == self.tail:
            self.tail, dll_node.prev.next = dll_node.prev, None
        else:
            dll_node.prev.next, dll_node.next.prev = dll_node.next, dll_node.prev
    
    def insert_node_at_end(self, dll_node):
        print(f"Node to be inserted end Key: {dll_node.key}, Value: {dll_node.val}")
        dll_node.prev, dll_node.next, self.tail.next, self.tail = self.tail, None, dll_node, dll_node



