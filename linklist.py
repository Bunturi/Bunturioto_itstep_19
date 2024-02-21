class Node:
    def __init__(self, data):
        # Initializing a Node with data and setting next pointer to None
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        # Initializing an empty linked list with head pointing to None
        self.head = None

    def append(self, data):
        # Adding a new node to the end of the linked list
        new_node = Node(data)

        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = new_node
            return