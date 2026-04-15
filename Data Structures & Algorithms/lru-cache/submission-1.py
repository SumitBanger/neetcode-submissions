class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val, self.next, self.prev = key, val, next, prev
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # Hashmap containing Key Value Pairs
        self.maxLength = capacity
        self.head = None
        self.tail = None    

    def remove(self, currentNode):
        nextEle = currentNode.next
        prevEle = currentNode.prev
        if self.tail == currentNode:
            nextEle.prev = prevEle
            self.tail = nextEle
        else:
        # Join the previous and next elements to each other 
            nextEle.prev = prevEle
            prevEle.next = nextEle        
    
    def insert(self, currentNode):
        # Add this element to the front of list (at head)
        oldMostRecent = self.head
        oldMostRecent.next = currentNode
        currentNode.prev = oldMostRecent
        self.head = currentNode

    def get(self, key: int) -> int:
        if key in self.cache:
            currentNode = self.cache[key]
            value = currentNode.val

            if self.head != currentNode:
                self.remove(currentNode)
                self.insert(currentNode)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        currentNode = ListNode(key, value)
        if self.head == None and self.tail == None:
            self.head = currentNode
            self.tail = currentNode

        if key not in self.cache:
            if len(self.cache) == self.maxLength: # we need to evict the LRU KeyValue Pair first
                lruElement = self.tail
                self.remove(lruElement)
                del self.cache[lruElement.key]
            
            self.cache[key] = currentNode

            # Add this element to the front of list (at head)
            self.insert(currentNode)
        else:
            currentNode = self.cache[key]
            currentNode.val = value

            if self.head != currentNode:
                self.remove(currentNode)
                self.insert(currentNode)
        
