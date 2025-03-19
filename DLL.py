# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

# Define a Doubly Linked List (DLL)
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # 1️⃣ Insert at the beginning
    def add_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If list is empty
            self.head = new_node
        else:
            new_node.next = self.head  # New node points to the current head
            self.head.prev = new_node  # Current head points back to new node
            self.head = new_node  # Update head to the new node

    # 2️⃣ Insert at the end
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty, set new node as head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link last node to new node
            new_node.prev = current  # New node points back to last node

    # 3️⃣ Insert after a specific node
    def add_after(self, data, target):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current and current.data != target:
            current = current.next
        if current is None:
            print(f"Node with value {target} not found!")
            return
        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # 4️⃣ Insert before a specific node
    def add_before(self, data, target):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current and current.data != target:
            current = current.next
        if current is None:
            print(f"Node with value {target} not found!")
            return
        new_node = Node(data)
        new_node.next = current
        new_node.prev = current.prev
        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node  # If inserting before the first node, update head
        current.prev = new_node

    # 5️⃣ Delete the first node
    def delete_first(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next is None:  # If only one node is present
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # 6️⃣ Delete the last node
    def delete_last(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None

    # 7️⃣ Delete a node by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current and current.data != value:
            current = current.next
        if current is None:
            print(f"Node with value {value} not found!")
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next  # If deleting the head node
        if current.next:
            current.next.prev = current.prev

    # 8️⃣ Print the list (Forward)
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("End")

    # 9️⃣ Print the list (Backward)
    def print_backward(self):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current.next:
            current = current.next  # Move to last node
        while current:
            print(current.data, end=" <-- ")
            current = current.prev
        print("Start")

    # 🔟 Find the middle node
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            return slow.data
        return None

    # 1️⃣1️⃣ Reverse the linked list
    def reverse(self):
        current = self.head
        prev = None
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        if prev:
            self.head = prev.prev

    # 1️⃣2️⃣ Check if the list is a palindrome
    def is_palindrome(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values == values[::-1]

    # 1️⃣3️⃣ Rotate the list by k places
    def rotate(self, k):
        if self.head is None:
            return
        current = self.head
        count = 1
        while current.next:
            current = current.next
            count += 1
        k = k % count  # Adjust if k > length
        if k == 0:
            return
        current.next = self.head  # Make it circular
        self.head.prev = current
        for _ in range(count - k):
            current = current.next
        self.head = current.next
        self.head.prev = None
        current.next = None

    # 1️⃣4️⃣ Count the total number of nodes
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 1️⃣5️⃣ Clear the entire list
    def clear(self):
        self.head = None

    def remove_duplicates(self):
        if self.head is None:
            return
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                next_node = current.next  # Store next node before deleting
                self.delete_by_value(current.data)  # Delete duplicate node
                current = next_node  # Move to next node
            else:
                seen.add(current.data)
                current = current.next

# ------------------------------
# Example Usage
dll = DoublyLinkedList()

dll.add_at_beginning(50)
dll.add_at_beginning(40)
dll.add_at_end(60)
dll.add_after(45, 40)
dll.add_before(55, 60)

print("Forward Traversal:")
dll.print_forward()

print("\nBackward Traversal:")
dll.print_backward()

dll.delete_by_value(45)
print("\nAfter deleting 45:")
dll.print_forward()

print("\nMiddle Node:", dll.find_middle())

print("\nReversing the list:")
dll.reverse()
dll.print_forward()

print("\nIs Palindrome:", dll.is_palindrome())

print("\nRotating list by 2:")
dll.rotate(2)
dll.print_forward()

print("\nTotal Nodes:", dll.count_nodes())

dll.clear()
print("\nAfter clearing:")
dll.print_forward()
dll.remove_duplicates()




