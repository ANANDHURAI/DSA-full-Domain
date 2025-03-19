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

    def kth_smallest(self, k):
        def traverse(node):
            nonlocal k
            if not node:
                return None
            left = traverse(node.left)
            if left is not None:
                return left
            k -= 1
            if k == 0:
                return node.value
            return traverse(node.right)

        return traverse(self.root)

    def kth_largest(self, k):
        def traverse(node):
            nonlocal k
            if not node:
                return None
            right = traverse(node.right)
            if right is not None:
                return right
            k -= 1
            if k == 0:
                return node.value
            return traverse(node.left)

        return traverse(self.root)

    def closest_value(self, target):
        def closest(node, closest_value):
            if not node:
                return closest_value
            if abs(node.value - target) < abs(closest_value - target):
                closest_value = node.value
            if target < node.value:
                return closest(node.left, closest_value)
            elif target > node.value:
                return closest(node.right, closest_value)
            else:
                return closest_value

        return closest(self.root, self.root.value if self.root else float('inf'))

    def is_bst(self):
        def validate(node, min_value, max_value):
            if not node:  
                return True
            if not (min_value < node.value < max_value):  
                return False
            
            return (validate(node.left, min_value, node.value) and
                    validate(node.right, node.value, max_value))

        return validate(self.root, float('-inf'), float('inf'))

    # Additional Operations

    def depth(self):
        def max_depth(node):
            if not node:
                return 0
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            return max(left_depth, right_depth) + 1

        return max_depth(self.root)

    def size(self):
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        return count_nodes(self.root)

    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print("Level-order Traversal:", result)
        return result

    def is_balanced(self):
        def check(node):
            if not node:
                return 0  # Height of an empty tree is 0

            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  # Unbalanced tree

            return max(left, right) + 1  # Return height of subtree

        return check(self.root) != -1


    def min_value(self):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left
        return current.value

    def max_value(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    

    def is_subtree(self, subtree_root):
    # Helper function to serialize a tree
        def serialize(node):
            if not node:
                return "null"  # Represent null nodes as "null"
            # Serialize the tree in pre-order (root, left, right)
            return f"#{node.value} " + serialize(node.left) + " " + serialize(node.right)

        # Serialize the main tree and the subtree
        main_tree_serialized = serialize(self.root)
        subtree_serialized = serialize(subtree_root)

        return subtree_serialized in main_tree_serialized

    
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
bst.level_order_traversal()
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


