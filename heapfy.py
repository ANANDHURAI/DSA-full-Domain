def heapify(arr, n, i):
    """Heapify a subtree rooted at index `i`."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    """Sort an array using Heap Sort."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example Usage
arr = [9, 4, 3, 8, 10, 2, 5]
heap_sort(arr)
print("Sorted array:", arr)  # Output: Sorted array: [2, 3, 4, 5, 8, 9, 10]




class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)  # Add the value to the end of the heap
        self._heapify_up(len(self.heap) - 1)  # Restore the heap property

    def remove(self):
        """Remove and return the smallest value (root) from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap the root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_value = self.heap.pop()  # Remove the smallest value
        self._heapify_down(0)  # Restore the heap property
        return min_value

    def _heapify_up(self, index):
        """Move the element at `index` up to its correct position."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)  # Recursively heapify up

    def _heapify_down(self, index):
        """Move the element at `index` down to its correct position."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Find the smallest among the current node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and heapify down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def display(self):
        """Display the heap."""
        print("Min-Heap:", self.heap)
        


# Example Usage
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.display()  # Output: Min-Heap: [1, 3, 8, 5]

print("Removed:", min_heap.remove())  # Output: Removed: 1
min_heap.display()  # Output: Min-Heap: [3, 5, 8]



class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)  # Add the value to the end of the heap
        self._heapify_up(len(self.heap) - 1)  # Restore the heap property

    def remove(self):
        """Remove and return the largest value (root) from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap the root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()  # Remove the largest value
        self._heapify_down(0)  # Restore the heap property
        return max_value

    def _heapify_up(self, index):
        """Move the element at `index` up to its correct position."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)  # Recursively heapify up

    def _heapify_down(self, index):
        """Move the element at `index` down to its correct position."""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Find the largest among the current node and its children
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not the current node, swap and heapify down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def display(self):
        """Display the heap."""
        print("Max-Heap:", self.heap)


# Example Usage
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(8)
max_heap.insert(1)
max_heap.display()  # Output: Max-Heap: [8, 3, 5, 1]

print("Removed:", max_heap.remove())  # Output: Removed: 8
max_heap.display()  # Output: Max-Heap: [5, 3, 1]




from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # BFS Traversal
    def bfs(self):
        queue = deque([self])  # Start with the root node in the queue
        while queue:
            current = queue.popleft()  # Get the first node in the queue
            print(current.key, end=' ')
            if current.left:
                queue.append(current.left)  # Add left child to queue
            if current.right:
                queue.append(current.right)  # Add right child to queue


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nBFS Traversal:")
root.bfs()  # Output: 1 2 3 4 5