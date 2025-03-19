class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Head pointer (starts as None for an empty list)

    # Add a node at the beginning of the list
    def add_begin(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            new_node.next = new_node  # Point the new node to itself
            self.head = new_node  # Update the head to the new node
        else:
            new_node.next = self.head  # Point the new node to the current head
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Point the last node to the new node
            self.head = new_node  # Update the head to the new node

    # Add a node at the end of the list
    def add_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            new_node.next = new_node  # Point the new node to itself
            self.head = new_node  # Update the head to the new node
        else:
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Point the last node to the new node
            new_node.next = self.head  # Point the new node to the head

    # Add a node after a specific node
    def add_after(self, data, check_data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            print("Circular Linked List is empty!")
            return
        current = self.head
        while True:
            if current.data == check_data:  # Find the node with the given data
                new_node.next = current.next  # Point the new node to the next node
                current.next = new_node  # Point the current node to the new node
                return
            current = current.next
            if current == self.head:  # If we've traversed the entire list
                break
        print(f"Node with data {check_data} not found!")

    # Add a node before a specific node
    def add_before(self, data, check_data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            print("Circular Linked List is empty!")
            return
        if self.head.data == check_data:  # If the head is the target, add at the beginning
            self.add_begin(data)
            return
        current = self.head
        while True:
            if current.next.data == check_data:  # Find the node before the target
                new_node.next = current.next  # Point the new node to the target node
                current.next = new_node  # Point the current node to the new node
                return
            current = current.next
            if current == self.head:  # If we've traversed the entire list
                break
        print(f"Node with data {check_data} not found!")

    # Delete the first node
    def delete_begin(self):
        if self.head is None:  # If the list is empty
            print("Circular Linked List is empty!")
        elif self.head.next == self.head:  # If there's only one node
            self.head = None
        else:
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = self.head.next  # Point the last node to the second node
            self.head = self.head.next  # Update the head to the second node

    # Delete the last node
    def delete_end(self):
        if self.head is None:  # If the list is empty
            print("Circular Linked List is empty!")
        elif self.head.next == self.head:  # If there's only one node
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:  # Traverse to the second last node
                current = current.next
            current.next = self.head  # Point the second last node to the head

    # Delete a specific node by value
    def delete_value(self, del_value):
        if self.head is None:  # If the list is empty
            print("Circular Linked List is empty!")
            return
        if self.head.data == del_value:  # If the head is the target, delete it
            self.delete_begin()
            return
        current = self.head
        while True:
            if current.next.data == del_value:  # Find the node before the target
                current.next = current.next.next  # Skip the target node
                return
            current = current.next
            if current == self.head:  # If we've traversed the entire list
                break
        print(f"Node with data {del_value} not found!")

    # Search for a node by value
    def search(self, target):
        if self.head is None:  # If the list is empty
            return False
        current = self.head
        while True:
            if current.data == target:  # If the target is found
                return True
            current = current.next
            if current == self.head:  # If we've traversed the entire list
                break
        return False  # If the target is not found

    # Print all nodes in the list
    def print_all(self):
        if self.head is None:  # If the list is empty
            print("Circular Linked List is empty!")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")  # Print the current node's data
            current = current.next
            if current == self.head:  # Stop when we reach the head again
                break
        print("Head")  # Indicate the end of the list

    # Count the number of nodes in the list
    def count_nodes(self):
        if self.head is None:  # If the list is empty
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:  # Stop when we reach the head again
                break
        return count

    # Clear the entire list
    def clear(self):
        self.head = None  # Reset the head to None

# Example usage:
cll = CircularLinkedList()
cll.add_begin(90)
cll.add_begin(80)
cll.add_end(100)
cll.add_after(1000, 90)
cll.add_before(8000, 90)
cll.print_all()  # Output: 80 -> 8000 -> 90 -> 1000 -> 100 -> Head

# Search operation
print("Search for 90:", cll.search(90))  # Output: Search for 90: True
print("Search for 200:", cll.search(200))  # Output: Search for 200: False

cll.delete_begin()
cll.print_all()  # Output: 8000 -> 90 -> 1000 -> 100 -> Head
cll.delete_end()
cll.print_all()  # Output: 8000 -> 90 -> 1000 -> Head
cll.delete_value(90)
cll.print_all()  # Output: 8000 -> 1000 -> Head
print("Number of nodes:", cll.count_nodes())  # Output: Number of nodes: 2
cll.clear()
cll.print_all()  # Output: Circular Linked List is empty!