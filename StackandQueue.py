class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if self.is_empty():
            print('Stack is empty!')
            return None
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            print('Stack is empty!')
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data
    
    def display(self):
        if self.is_empty():
            print('Stack is empty!')
            return
        else:
            current = self.top
            while current:
                print(current.data, end=' -> ')
                current = current.next
            print('END')

    # Advanced Operations

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def search(self, target):
        current = self.top
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def clear(self):
        self.top = None

    def min_element(self):
        if self.is_empty():
            print('Stack is empty!')
            return None
        current = self.top
        min_val = current.data
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def max_element(self):
        if self.is_empty():
            print('Stack is empty!')
            return None
        current = self.top
        max_val = current.data
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

# Create a stack and perform operations
stck = Stack()

stck.push(10)
stck.push(20)
stck.push(30)
stck.push(40)
stck.push(50)
stck.push(60)

print("Stack after pushes:")
stck.display()

print("Popped element:", stck.pop())
print("Peeked element:", stck.peek())
print("Is stack empty?", stck.is_empty())
print("Size of stack:", stck.size())
print("Search for 30:", stck.search(30))
print("Search for 100:", stck.search(100))
print("Minimum element:", stck.min_element())
print("Maximum element:", stck.max_element())

stck.clear()
print("Stack after clearing:")
stck.display()



from collections import deque

class QueueToStack:
    def __init__(self):
        self.queue1 = deque()  # This queue is used for push operation
        self.queue2 = deque()  # This queue is used for pop operation

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        popped_item = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_item

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        top_item = self.queue1.popleft()
        self.queue2.append(top_item) 

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item

    def is_empty(self):
        return len(self.queue1) == 0 and len(self.queue2) == 0

    def size(self):
        return len(self.queue1) + len(self.queue2)
    


# Example usage:
stack = QueueToStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2
print(stack.size()) # Output: 2






def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if not ((char == ")" and top == "(") or
                    (char == "}" and top == "{") or
                    (char == "]" and top == "[")):
                return False
    return len(stack) == 0

# Example
print(is_balanced("{[()]}"))  
print(is_balanced("{[(])}"))  


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    def peek(self):
        if self.is_empty():
            print('Queue is empty!')
            return None
        return self.front.data
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty!')
            return None
        else:
            dequeued_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_data
    
    def display(self):
        if self.is_empty():
            print('Queue is empty!')
            return
        else:
            current = self.front
            while current:
                print(current.data, end=' -> ')
                current = current.next
            print('END')

    # Advanced Operations

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
    
    def is_full(self):
        return self.max_size is not None and self.current_size >= self.max_size

    def search(self, target):
        current = self.front
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def clear(self):
        self.front = self.rear = None

    def min_element(self):
        if self.is_empty():
            print('Queue is empty!')
            return None
        current = self.front
        min_val = current.data
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def max_element(self):
        if self.is_empty():
            print('Queue is empty!')
            return None
        current = self.front
        max_val = current.data
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

# Create a queue and perform operations
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

print("Queue after enqueues:")
queue.display()

print("Dequeued element:", queue.dequeue())
print("Peeked element:", queue.peek())
print("Is queue empty?", queue.is_empty())
print("Size of queue:", queue.size())
print("Search for 30:", queue.search(30))
print("Search for 100:", queue.search(100))
print("Minimum element:", queue.min_element())
print("Maximum element:", queue.max_element())

queue.clear()
print("Queue after clearing:")
queue.display()






from collections import deque

class QueueToStack:
    def __init__(self):
        self.queue = deque()  # Use a single queue

    def push(self, item):
        # Add the new item to the queue
        self.queue.append(item)
        # Rotate the queue to bring the new item to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
stack = QueueToStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2
print(stack.size()) # Output: 2




class StackToQueue:
    def __init__(self):
        self.stack1 = []  # Used for enqueue
        self.stack2 = []  # Used for dequeue

    def enqueue(self, item):
        # Simply push the item to stack1
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Peek from stack2
        return self.stack2[-1]

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Example usage:
queue = StackToQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.peek())     # Output: 2
print(queue.size())     # Output: 
