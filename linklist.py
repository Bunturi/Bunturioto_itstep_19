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