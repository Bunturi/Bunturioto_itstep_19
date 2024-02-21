class Node:
    def __init__(self, data):
        # Initializing a Node with data and setting next pointer to None
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        # Initializing an empty linked list with head pointing to None
        self.head = None