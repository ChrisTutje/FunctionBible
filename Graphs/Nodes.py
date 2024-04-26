class SingleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class DoubleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
BinarytreeNode = DoubleLinkedNode

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = set()