from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insertion(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        while True:
            if data < current.value:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right

    def searching(self, data):
        current = self.root
        while current:
            if current.value == data:
                print("Data found!")
                return True
            elif data < current.value:
                current = current.left
            else:
                current = current.right
        print("Data not found.")
        return False

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, current, data):
        if not current:
            print("Data not found.")
            return current

        if data < current.value:
            current.left = self._delete(current.left, data)
        elif data > current.value:
            current.right = self._delete(current.right, data)
        else:
            if not current.left:
                return current.right
            if not current.right:
                return current.left

            temp = current.right
            while temp.left:
                temp = temp.left  # Find in-order successor
            current.value = temp.value
            current.right = self._delete(current.right, temp.value)
        return current

    def pre_order(self):
        def traverse(node):
            if not node:
                return
            print(node.value, end=" ")
            traverse(node.left)
            traverse(node.right)

        print("Pre-order Traversal:", end=" ")
        traverse(self.root)
        print()

    def inorder(self):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            print(node.value, end=" ")
            traverse(node.right)

        print("In-order Traversal:", end=" ")
        traverse(self.root)
        print()

    def postorder(self):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            print(node.value, end=" ")

        print("Post-order Traversal:", end=" ")
        traverse(self.root)
        print()

    
    def kth_smallest(self,k):
        stack = []
        current = self.root
        
        while True:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            
            k-= 1 
            if k ==0 :
                return current.value
            
            current = current.right

    def kth_largest(self,k):
        stack = []
        current = self.root
        
        while True:
            while current:
                stack.append(current)
                current = current.right
            current = stack.pop()
            
            k-=1 
            if k == 0 :
                return current.value
            
            current = current.left

    def  closest_value(self , target):
        current = self.root
        cloest_value = float('inf')
        
        while current:
            if abs(current.value - target) < abs(cloest_value - target):
                cloest_value = current.value
            
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            
            else:
                return current.value
                
        return cloest_value
    

    def is_bst(self):
        current = self.root
        stack = [(current , float('-inf') , float('inf'))]
        
        while stack:
            node , min_value , max_val = stack.pop()
            if not(min_value < node.value < max_val):
                return False
            
            if node.left:
                stack.append((node.left , min_value , node.value))
                
            if node.right:
                stack.append((node.right , node.value , max_val))
                
                
        return True


    def depth(self):
        if not self.root:
            return 0 
        
        stack = [(self.root , 1)]
        max_depth = 0
        while stack:
            node , depth = stack.pop()
            
            max_depth = max(max_depth , depth)
            
            if node.left:
                stack.append((node.left , depth +1 ))
            if node.right:
                stack.append((node.right , depth +1 ))
                
        return max_depth

    def size(self):
        stack = [self.root]
        count = 0 
        
        while stack:
            node = stack.pop()
            count += 1 
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
        return count

    def BFS(self):
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result

    def is_balanced(self):
        stack = [(self.root , False)]
        hights = {}
        
        while stack:
            node , visited = stack.pop()
            if not node:
                continue
            
            if visited:
                
                left_hight = hights.get(node.left , 0)
                right_hight = hights.get(node.right , 0)
                
                if abs(left_hight - right_hight) > 1 :
                    return False
                
                hights[node] = max(left_hight, right_hight) +1 
                
            else:
                stack.append((node ,True))
                stack.append((node.right , False))
                stack.append((node.left, False))
            
        return True 


    def min_value(self):
        current = self.root
            
        while current.left:
            current = current.left
        return current.value
            
    def max_value(self):
        current = self.root
            
        while current.right:
            current = current.right
        return current.value
    
    

    def is_subtree(self , subtree_root):
        if not subtree_root:
            return True
        
        if not self.root:
            return False
            
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            if node.value == subtree_root.value and self.is_subtree_helper(node , subtree_root):
                return True
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return False
        
    def is_subtree_helper(self , node1 ,node2):
        stack = [(node1 , node2)]
        
        while stack:
            n1,n2 = stack.pop()
            if not n1 and not n2:
                continue
            
            if not n1 or not n2 or n1.value != n2.value:
                return False
                
            stack.append((n1.left , n2.left))
            stack.append((n1.right , n2.right))
            
        return True

    
# Example Usage
bst = BST()
bst.insertion(20)
bst.insertion(10)
bst.insertion(5)
bst.insertion(30)
bst.insertion(25)
bst.insertion(35)
bst.searching(30)

bst.pre_order()
bst.inorder()
bst.postorder()

k = 1
print(f"The {k}rd smallest element is:", bst.kth_smallest(k))
print(f"The {k}rd largest element is:", bst.kth_largest(k))

target = 24
print(f"Closest value to {target}:", bst.closest_value(target))

print("Is the tree a valid BST?", bst.is_bst())

# Testing additional operations
print("Depth of the tree:", bst.depth())
print("Size of the tree:", bst.size())
bst.BFS()
print("Is the tree balanced?", bst.is_balanced())
print("Minimum value in the tree:", bst.min_value())
print("Maximum value in the tree:", bst.max_value())

bst = BST()
bst.insertion(20)
bst.insertion(10)
bst.insertion(30)
bst.insertion(5)
bst.insertion(15)
bst.insertion(25)
bst.insertion(35)

# Check if two trees are identical
bst2 = BST()
bst2.insertion(20)
bst2.insertion(10)
bst2.insertion(30)

bst.inorder()  # Should print in reverse order


subtree = Node(4)
subtree.left = Node(1)
subtree.right = Node(2)

# Check if the subtree exists in the main BST
result = bst.is_subtree(subtree)
print("Is subtree present?", result) 


