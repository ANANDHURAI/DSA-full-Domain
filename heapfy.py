def heapify(arr, n, i):
    
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

   
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest) 

def heap_sort(arr):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)


arr = [9, 4, 3, 8, 10, 2, 5]
heap_sort(arr)
print("Sorted array:", arr)




class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
      
        self.heap.append(value) 
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_value = self.heap.pop()  
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
     
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)  

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def display(self):
      
        print("Min-Heap:", self.heap)
        


# Example Usage
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)
min_heap.display()

print("Removed:", min_heap.remove()) 
min_heap.display() 



class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop() 
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
       
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent) 

    def _heapify_down(self, index):
    
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

       
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def display(self):
        print("Max-Heap:", self.heap)


# Example Usage
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(8)
max_heap.insert(1)
max_heap.display()  

print("Removed:", max_heap.remove())  
max_heap.display() 




from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

   
    def bfs(self):
        queue = deque([self])
        while queue:
            current = queue.popleft() 
            print(current.key, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nBFS Traversal:")
root.bfs()