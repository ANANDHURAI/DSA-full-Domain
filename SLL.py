class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Head pointer (starts as None for an empty list)

    # Add a node at the beginning of the list
    def add_begin(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node

    # Add a node at the end of the list
    def add_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Point the last node to the new node

    # Add a node after a specific node
    def add_after(self, data, check_data):
        new_node = Node(data)  # Create a new node
        current = self.head
        while current:
            if current.data == check_data:  # Find the node with the given data
                new_node.next = current.next  # Point the new node to the next node
                current.next = new_node  # Point the current node to the new node
                return
            current = current.next
        print(f"Node with data {check_data} not found!")

    # Add a node before a specific node
    def add_before(self, data, check_data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, print a message
            print("Linked List is empty!")
            return
        if self.head.data == check_data:  # If the head is the target, add at the beginning
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.data == check_data:  # Find the node before the target
                new_node.next = current.next  # Point the new node to the target node
                current.next = new_node  # Point the current node to the new node
                return
            current = current.next
        print(f"Node with data {check_data} not found!")

    # Delete the first node
    def delete_begin(self):
        if self.head is None:  # If the list is empty, print a message
            print("Linked List is empty!")
        else:
            self.head = self.head.next  # Update the head to the next node

    # Delete the last node
    def delete_end(self):
        if self.head is None:  # If the list is empty, print a message
            print("Linked List is empty!")
        elif self.head.next is None:  # If there's only one node, delete it
            self.head = None
        else:
            current = self.head
            while current.next.next:  # Traverse to the second last node
                current = current.next
            current.next = None  # Remove the last node

    # Delete a specific node by value
    def delete_value(self, del_value):
        if self.head is None:  # If the list is empty, print a message
            print("Linked List is empty!")
            return
        if self.head.data == del_value:  # If the head is the target, delete it
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == del_value:  # Find the node before the target
                current.next = current.next.next  # Skip the target node
                return
            current = current.next
        print(f"Node with data {del_value} not found!")

    # Print all nodes in the list
    def print_all(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the current node's data
            current = current.next
        print("End")  # Indicate the end of the list

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev to the current node
            current = next_node  # Move current to the next node
        self.head = prev  # Update the head to the last node

    # Find the middle node of the list
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:  # Move slow by 1 step and fast by 2 steps
            slow = slow.next
            fast = fast.next.next
        return slow.data  # Return the middle node's data

    # Check if the list is a palindrome
    def is_palindrome(self):
        stack = []
        current = self.head
        while current:  # Push all node data into a stack
            stack.append(current.data)
            current = current.next
        current = self.head
        while current:  # Compare stack data with node data
            if current.data != stack.pop():
                return False
            current = current.next
        return True

    # Rotate the list by k positions
    def rotate(self, k):
        if not self.head:
            return
        current = self.head
        count = 1
        while current.next:  # Traverse to the last node
            current = current.next
            count += 1
        current.next = self.head  # Make the list circular
        k = k % count  # Handle cases where k > count
        current = self.head
        for _ in range(count - k - 1):  # Traverse to the new tail
            current = current.next
        self.head = current.next  # Update the head
        current.next = None  # Break the circular link

    # Swap two nodes by their values
    def swap_nodes(self, x, y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX and currX.data != x:  # Find node X and its previous node
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY and currY.data != y:  # Find node Y and its previous node
            prevY = currY
            currY = currY.next
        if not currX or not currY:  # If either node is not found, return
            return
        if prevX:  # Update previous node's next pointer for X
            prevX.next = currY
        else:
            self.head = currY
        if prevY:  # Update previous node's next pointer for Y
            prevY.next = currX
        else:
            self.head = currX
        temp = currX.next  # Swap the next pointers of X and Y
        currX.next = currY.next
        currY.next = temp

    # Count the number of nodes in the list
    def count_nodes(self):
        current = self.head
        count = 0
        while current:  # Traverse the list and count nodes
            count += 1
            current = current.next
        return count

    # Clear the entire list
    def clear(self):
        self.head = None  # Reset the head to None

# Example usage:
sll = SinglyLinkedList()
sll.add_begin(90)
sll.add_begin(80)
sll.add_end(100)
sll.add_after(1000, 90)
sll.add_before(8000, 90)
sll.print_all()  # Output: 80 -> 8000 -> 90 -> 1000 -> 100 -> End
sll.reverse()
sll.print_all()  # Output: 100 -> 1000 -> 90 -> 8000 -> 80 -> End
print("Middle node:", sll.find_middle())  # Output: Middle node: 90
print("Is palindrome:", sll.is_palindrome())  # Output: Is palindrome: False
sll.rotate(4)
sll.print_all()  # Output: 8000 -> 80 -> 100 -> 1000 -> 90 -> End
sll.swap_nodes(80, 100)
sll.print_all()  # Output: 8000 -> 100 -> 80 -> 1000 -> 90 -> End
print("Number of nodes:", sll.count_nodes())  # Output: Number of nodes: 5
sll.clear()
sll.print_all()  # Output: End