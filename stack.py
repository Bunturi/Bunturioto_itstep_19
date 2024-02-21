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

    def top(self):
        # Return the data of the top node without removing it
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("stack is empty")

    def size(self):
        # Return the size of the stack
        return self.length

    def push(self, data):
        # Push a new node with data onto the stack
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    def pop(self):
        # Remove and return the data of the top node
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("stack is empty")

    def insert(self, data, index):
        # Insert a new element at the specified index
        if index < 0 or index > self.length:
            raise IndexError("index out of range")

        if index == 0:
            # If index is 0, simply push the new element onto the stack
            self.push(data)
        else:
            # Traverse the stack to find the node at the index before the desired position
            current_node = self.top_node
            for _ in range(index - 1):
                current_node = current_node.next

            # Create a new node with the data
            new_node = Node(data)

            # Adjust pointers to insert the new node at the specified index
            new_node.next = current_node.next
            current_node.next = new_node

            # resize the length of the stack
            self.length += 1


# Test the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.size())  # Print the size of the stack before insert
stack.insert(5, 2)  # Insert 5 at index 2
print(stack.size())  # Print the size of the stack
print(stack.top())
