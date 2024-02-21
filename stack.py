class Node:
    def __init__(self, data):
        # Initialize a node with data and set next pointer to None
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Initialize an empty stack with top_node pointing to None and length set to 0
        self.top_node = None
        self.length = 0

    def empty(self):
        # Check if the stack is empty
        return self.length == 0
