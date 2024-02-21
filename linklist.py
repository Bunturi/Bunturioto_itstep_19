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

        # Traverse the list to find the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Point the last node's next to the new node
        last_node.next = new_node

    def display_info(self):
        # Displaying the elements of the linked list
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()

    def insert(self, data, index):
        # Inserting a new node at a specified index
        new_node = Node(data)

        if index == 0:
            # If index is 0, insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to the node at the index before the desired position
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        # Insert the new node at the specified index
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        # Removing a node with a specified data value
        if self.head is None:
            # If the list is empty, return
            return

        if self.head.data == data:
            # If the data is in the head node, remove the head
            self.head = self.head.next
            return

        # Traverse the list to find the node before the node to be removed
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        # If the node with data is found, remove it
        if current_node.next:
            current_node.next = current_node.next.next