# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2

#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])

#     return list(merge(left , right))

# def merge(left , right):
#     result = []
#     while len(left) != 0 and len(right) != 0:
#         if left[0] < right[0] :
#             result.append(left[0])
#             left.remove(left[0])
#         else:
#             result.append(right[0])
#             right.remove(right[0])

#     if len(left) == 0 :
#         result  = result + right
#     else:
#         result = result + left
    
#     return result

# arr1 = [32,13,23,54]
# arr2 = [76,45,23,21]
# num = arr1 + arr2
# print('merge sort:',mergesort(num))


# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr)//2]
#     left = [i for i in arr if i < pivot]
#     middle = [i for i in arr if i == pivot]
#     right = [i for i in arr if i > pivot]

#     return quickSort(left) + middle + quickSort(right)

# arr1 = [32,13,23,54]
# arr2 = [76,45,23,21]
# num = arr1 + arr2
# print('quick sort :',quickSort(num))



# def bubblesort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1 , len(arr)):
#             if arr[i] > arr[j] :
#                 arr[i] , arr[j] = arr[j] , arr[i]

#     return arr
# arr1 = [32,13,23,54]
# arr2 = [76,45,23,21]
# num = arr1 + arr2
# print('bubblesort : ', bubblesort(num))


# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j] :
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#     return arr

# arr1 = [32,13,23,54]
# arr2 = [76,45,23,21]
# num = arr1 + arr2
# print('insertionsort : ', insertionsort(num))

# def selectionsort(arr):
#     for i in range(len(arr)):
#         min_index = i

#         for j in range(i+1 , len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i] ,arr[min_index] = arr[min_index] ,arr[i]
#     return arr

# arr1 = [32,13,23,54]
# arr2 = [76,45,23,21]
# num = arr1 + arr2
# print('selectionsort : ', selectionsort(num))
        


# def heapsort(arr):
#     n = len(arr)
#     for i in range(n//2-1 , -1 , -1):
#         heapify(arr , n , i)

#     for i in range(n-1 , 0 , -1):
#         arr[0] ,arr[i] = arr[i] ,arr[0]
#         heapify(arr , i ,0)


# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)


# arr1 = [32,13,23,54]
# arr2 = [76,45,23,21]
# num = arr1 + arr2

# heapsort(num)
# print('heapsort :', num)

# from collections import deque

# class GraphDataStracture:
#     def __init__(self ,wieght=False , direct=False):
#         self.direct = direct
#         self.wieght = wieght
#         self.graph = {}

#     def add_verdex(self , vertex):
#         if vertex not in self.graph:
#             if self.wieght:
#                 self.graph[vertex] = {}
#             else:
#                 self.graph[vertex] = []
#         else:
#             return 'already this value thire'
    
#     def add_edges(self, v1 ,v2 ,w):
#         if v1 in self.graph and v2 in self.graph:
#             if self.wieght:
#                 self.graph[v1][v2] = w
#                 if not self.direct:
#                     self.graph[v2][v1] = w
#             else:
#                 self.graph[v1].append(v2)
#                 if not self.direct:
#                     self.graph[v2].append(v1)



#     def remove_edge(self,v1 , v2):
#         if v1 in self.graph and v2 in self.graph[v1]:
#             if self.wieght:
#                 del self.graph[v1][v2] 
#                 if not self.direct:
#                     del self.graph[v2][v1]
#             else:
#                 self.graph[v1].remove(v2)
#                 if not self.direct:
#                     self.graph[v2].remove(v1)

#     def remove_vertex(self , vertex):
#         if vertex in self.graph:
#             del self.graph[vertex]
#             for v in self.graph:
#                 if vertex in self.graph[v]:
#                     if self.wieght:
#                         del self.graph[v][vertex]
#                     else:
#                         self.graph[v].remove(vertex)

#     def display(self):
#         for vert,edg in self.graph.items():
#             print(vert , '->',edg)

#     def dfs(self ,start ,visit=None):
#         if visit is None:
#             visit = []
#         if start not in visit:
#             visit.append(start)
#             for neibours in self.graph[start]:
#                 self.dfs(neibours , visit)
#         return visit

         
#     def bfs(self , start):
#         visited = set()
#         queue = deque([start])
#         result = []
#         while queue:
#             node = queue.popleft()
#             if node not in visited:
#                 visited.add(node)
#                 result.append(node)
#                 for neibours in self.graph[node]:
#                     if neibours not in visited:
#                         queue.append(neibours)
#         return result
    
#     def is_finite(self):
#         return len(self.graph) < float('inf')
    
#     def is_trancitive(self):
#         return len(self.graph) == 1
    
#     def is_direct_graph(self):
#         return not self.direct
    
#     def is_wight_graph(self):
#         return not self.wieght
    
#     def is_simple(self):
#         for vertex in self.graph:
#             if self.wieght:
#                 if vertex in self.graph[vertex]:
#                     return False
#             else:
#                 if vertex in self.graph[vertex]:
#                     return False
#                 if len(self.graph([vertex])) != len(set(self.graph([vertex]))):
#                     return False
#         return True
    
#     def is_milti_graph(self):
#         for vert in self.graph:
#             if self.wieght == False and len(self.graph[vert]) == len(set(self.graph[vert])):
#                 return True
#         return False
    
#     def is_null_graph(self):
#         for vert in self.graph:
#             if self.graph[vert]:
#                 return False
#         return True
    
#     def is_complete(self):
#         n = len(self.graph)
#         for vert in self.graph:
#             if self.graph[vert] != n-1:
#                 return False
#         return True
    
#     def is_regular(self):
#         deggres = [len(self.graph[vert]) for vert in self.graph]
#         print(deggres)
#         return all(deg == deggres[0] for deg in deggres)
    
#     def is_connected_graph(self):
#         visted = set()
#         start_vertex = next(iter(self.graph))
#         stack = [start_vertex]
#         while stack:
#             vert = stack.pop()
#             if vert not in visted:
#                 visted.add(vert)
#                 if self.wieght:
#                     stack.extend(self.graph[vert].keys())
#                 else:
#                     stack.extend(self.graph[vert])
#         return len(self.graph) == len(visted)

#     def is_cyclic(self):
#         def dfs(vertex, visited, rec_stack):
#             visited.add(vertex)
#             rec_stack.add(vertex)

#             for neighbor in self.graph[vertex]: 
#                 if neighbor not in visited:
#                     if dfs(neighbor, visited, rec_stack):  # Recursively visit
#                         return True
#                 elif neighbor in rec_stack:  # Cycle detected
#                     return True

#             rec_stack.remove(vertex)  # Remove from recursion stack after processing
#             return False

#         visited = set()
#         rec_stack = set()
        
#         for vertex in self.graph:
#             if vertex not in visited:
#                 if dfs(vertex, visited, rec_stack):
#                     return True  # Cycle found
                    
#         return False  # No cycle detected
    
#     def dag(self):
#         return self.direct and not self.is_cyclic()
    
#     def is_subgraph(self , other_graph):
#         for vert in other_graph.graph:
#             if vert not in self.graph:
#                 return False
            
#             main_neibours = self.graph[vert]
#             sub_neibours = other_graph.graph[vert]

#             if any(neibour not in main_neibours for neibour in sub_neibours):
#                 return False
            
#             elif isinstance(sub_neibours , dict):
#                 for edge, w in sub_neibours.items():
#                     if main_neibours.get(edge) != w:
#                         return False
#         return True



# gra = GraphDataStracture(True , True)
# gra.add_verdex('A')
# gra.add_verdex('F')
# gra.add_verdex('D')
# gra.add_verdex('K')
# gra.add_edges('A','D',10)
# gra.add_edges('D','K',20)
# gra.add_edges('K','A',50)
# gra.add_edges('F','A',80)
# gra.display()
# print('##################')
# print('dfs',gra.dfs('A'))
# print('bfs:',gra.bfs('A'))
# print(gra.is_finite())
# print(gra.is_trancitive())
# print(gra.is_direct_graph())
# print(gra.is_wight_graph())
# print(gra.is_simple())
# print(gra.is_milti_graph())
# print(gra.is_null_graph())
# print('complete:',gra.is_complete())
# print('is_recular:',gra.is_regular())
# print('conected : ', gra.is_connected_graph())
# print('cyclic:' , gra.is_cyclic())
# print('dag', gra.dag())
# g1 = GraphDataStracture(direct=False , wieght=False)
# g1.add_verdex('A')
# g1.add_verdex('D')
# g1.add_verdex('F')
# g1.add_edges('A','D',10)
# g1.add_edges('F','A',80)
# print('is subgraph', gra.is_subgraph(g1))



# class HashTable:
#     def __init__(self ,size):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def hashing(self , key):
#         return sum(ord(char)for char in key) % self.size
    
#     def insertion(self , key ,value):
#         index = self.hashing(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key , value])

#     def deletion(self , key):
#         index = self.hashing(key)
#         for i , pair in enumerate(self.table[index]):
#             if pair[0] == key:
#                 del self.table[index][i]
#                 return True
#         return False
    
#     def search(self ,key):
#         index = self.hashing(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None
    
#     def display(self):
#         return self.table

# h = HashTable(5)
# h.insertion('anand' ,21)
# h.insertion('karthi',21)
# h.insertion('thiru',19)
# h.insertion('naveen',17)
# h.insertion('vithya',22)
# h.insertion('devi',227)
# print(h.display())
# h.deletion('thiru')
# print(h.display())
# print(h.search('anand'))



# class Hashtable:
#     def __init__(self , size) -> None:
#         self.size = size
#         self.table = [None] * size

#     def hashing(self , key):
#         hash_code =  sum(ord(char) for char in key) % self.size
#         print(hash_code)
#         return hash_code

#     def insertion(self ,key ,value):
#         index = self.hashing(key)
#         start_index = index

#         while self.table[index] is not None:
#             if self.table[index][0] == key:
#                 self.table[index] = (key , value)
#                 return 
#             index = (index +1) % self.size
#             if index == start_index:
#                 raise Exception('table is full!')
#         self.table[index] = (key , value)

#     def display(self):
#         return self.table
    

#     def deletion(self , key):
#         index = self.hashing(key)
#         start_index = index

#         while self.table[index] is not None:
#             if self.table[index][0] == key:
#                 self.table[index] = "deleted"
#                 return True
#             index = (index+1) % self.size
#             if index == start_index:
#                 break
#         return False

#     def search(self , key):
#         index = self.hashing(key)
#         start_index = index

#         while self.table[index] is not None:
#             if self.table[index][0] == key:
#                 return self.table[index][1]
#             index = index + 1 % self.size
#             if index == start_index:
#                 break
#         return None
    

# h1 = Hashtable(4)
# h1.insertion('arun', 22)
# h1.insertion('kanna', 23)
# h1.insertion('vasu',20)
# h1.insertion('varun',23)
# # h1.insertion('abi',23)
# print(h1.display())
# print(h1.search('vasu'))
# print(h1.deletion('vasu'))
# print(h1.display())


# class MaxHeap :
#     def __init__(self) -> None:
#         self.heap = []
    
#     def insert(self, data):
#         self.heap.append(data)
#         self.heapfy_up(len(self.heap)-1)

#     def heapfy_up(self , index):
#         parent = (index -1) // 2
#         if  parent >= 0 and self.heap[index] > self.heap[parent]:
#             self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
#             self.heapfy_up(parent)

#     def heapfy_down(self , index):
#         largest = index
#         left = 2 * index + 1 
#         right = 2 * index +2 

#         if left < len(self.heap) and self.heap[left] > self.heap[largest]:
#             largest = left
#         elif right < len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest = right

#         elif largest != index:
#             self.heap[largest] , self.heap[index] = self.heap[index] , self.heap[largest]
#             self.heapfy_down(largest)

    
#     def deletion(self):
#         if not self.heap:
#             print('heap is empty')
#             return None
        
#         if len(self.heap) == 1 :
#             return self.heap.pop()
        
#         self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]
#         max_ele = self.heap.pop()
#         self.heapfy_down(0)
#         return max_ele
    
#     def display(self):
#         return self.heap
    
# h = MaxHeap()
# h.insert(90)
# h.insert(650)
# h.insert(20)
# h.insert(80)
# h.insert(90)

# print(h.display())

# print(h.deletion())
# print(h.display())




# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# def dfs(start, visited=None):
#     if visited is None:  
#         visited = set()   

#     if start not in visited:
#         visited.add(start)
#         for neighbor in graph[start]:  
#             if neighbor not in visited:
#                 dfs(neighbor, visited)

#     return visited

# from collections import deque

# def bfs(start):
#     visited = set()
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:  
#                     queue.append(neighbor)

#     return visited

# # Testing
# print("DFS:", dfs('A'))  # Expected: {'A', 'B', 'D', 'E', 'F', 'C'}
# print("BFS:", bfs('A'))  # Expected: {'A', 'B', 'C', 'D', 'E', 'F'}
# from collections import deque

# class Node:
#     def __init__(self ,value) -> None:
#         self.value = value
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insertion(self , data):
#         if self.root is None:
#             self.root = Node(data)
#             return 
#         current = self.root
#         while True:
#             if data < current.value:
#                 if current.left is None:
#                     current.left =  Node(data)
#                     return
#                 current = current.left
#             else:
#                 if current.right is None:
#                     current.right = Node(data)
#                     return
#                 current = current.right
            
#     def searching(self , data):
#         current = self.root
#         while current:
#             if current.value == data:
#                 print('data found.')
#                 return True
#             elif current.value > data:
#                 current = current.left
#             else:
#                 current = current.right
#         print('data not found')
#         return False
    
#     def delete(self , data):
#         self.root = self.delete_helper(self.root , data)

#     def delete_helper(self , current , data):
#         if current is None:
#             return None
#         if data < current.value:
#             current.left = self.delete_helper(current.left , data)
#         elif data > current.value:
#             current.right = self.delete_helper(current.right , data)
#         else:
#             if not current.left:
#                 return current.right
#             elif not current.right:
#                 return current.left
            
#             else:
#                 temp = current.right
#                 while temp.left : 
#                     temp = temp.left
#                 current.value = temp.value
#                 current.right = self.delete_helper(current.right , temp.value)

#         return current
    
#     def pre_order(self):
#         def travarse(current):
#             if current is None:
#                 return 
#             print(current.value , end=" ")
#             travarse(current.left)
#             travarse(current.right)
#         print('pre order traversel')
#         travarse(self.root)
#         print()
        
#     def post_order(self):
#         def traverse(current):
#             if current is None:
#                 return 
#             traverse(current.left)
#             traverse(current.right)
#             print(current.value , end=" ")
#         print('post order')
#         traverse(self.root)
#         print()
    
#     def In_order(self):
#         def traverse(current):
#             if current is None:
#                 return 
#             traverse(current.left)
#             print(current.value , end=" ")
#             traverse(current.right)
#         print('in order tarevrse')
#         traverse(self.root)
#         print()

#     def k_largest_element(self , k):
#         def traverse(node):
#             nonlocal k
#             if not node:
#                 return None
#             right = traverse(node.right)
#             if right:
#                 return right
#             k -= 1
#             if k == 0 :
#                 return node.value
#             return traverse(node.left)
#         return traverse(self.root)
    
#     def k_smallest_element(self , k):
#         def traverse(node):
#             nonlocal k
#             if not node:
#                 return None
#             left = traverse(node.left)
#             if left :
#                 return left
#             k -= 1
#             if k == 0:
#                 return node.value
#             return traverse(node.right)
#         return traverse(self.root)
    
    
#     def closest_value_function(self, target):
#         def closest_helper(node, co_val):
#             if not node:
#                 return co_val  # Return the current closest value

#             if abs(node.value - target) < abs(co_val - target):
#                 co_val = node.value  # Update closest value

#             if target < node.value:
#                 return closest_helper(node.left, co_val)  # Move left
#             else:
#                 return closest_helper(node.right, co_val)  # Move right

#         return closest_helper(self.root, self.root.value if self.root else float('inf'))
    
#     def is_bst_bfs(self):
#         if not self.root:
#             return True
        
#         queue = deque([(self.root , float('-inf') , float('inf'))])
#         while queue:
#             node , min_value , max_val = queue.popleft()

#             if not(min_value < node.value < max_val):
#                 return False
#             if node.left:
#                 queue.append(node.left , min_value , node.value)
#             if node.left:
#                 queue.append(node.right , node.value , max_val)
#         return True
    
#     def min_value(self):
#         if not self.root:
#             return None
#         current = self.root
#         while current.left:
#             current = current.left
#         return current.value
    
#     def max_value(self):
#         if not self.root:
#             return None
#         current = self.root
#         while current.right:
#             current = current.right
#         return current.value
    
        
    

# b = BST()
# b.insertion(30)
# b.insertion(40)
# b.insertion(20)
# b.insertion(80)
# b.insertion(60)
# b.insertion(90)

# b.pre_order()
# b.In_order()
# b.post_order()

# b.delete(20)
# print('after deletiing')
# b.pre_order()

# print(b.searching(80))
# print(b.k_largest_element(3))
# print(b.k_smallest_element(2))
# print('cloest value:')
# print(b.closest_value_function(43))
# print(b.is_bst_bfs())
# print('min:' , b.min_value())
# print('max:' , b.max_value())
    

# from collections import deque

# class TrieNode:
#     def __init__(self) -> None:
#         self.children = {}
#         self.end = False

# class Trie:
#     def __init__(self) -> None:
#         self.root = TrieNode()

#     def insertion(self , word):
#         current = self.root
#         for char in word:
#             if char not in current.children:
#                 current.children[char] = TrieNode()
#             current = current.children[char]
#         current.end = True
        
#     def search(self , word):
#         current = self.root
#         for char in word:
#             if char not in current.children:
#                 return False
#             current = current.children[char]
#         return current.end
    
#     def delete(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False  # Word not found, no deletion needed
#             node = node.children[char]
#         if not node.end:
#             return False  
        
#         node.end = False  
#         return True 
    

#     def prefix_fuction(self , prefix):
#         current = self.root
#         for char in prefix:
#             if char not in current.children:
#                 return False
#             current = current.children[char]
#         return True
    
#     def count_fuction(self):
#         if not self.root:
#             return 0
#         queue = deque([self.root])
#         count = 0
#         while queue:
#             node = queue.popleft()
#             if node.end:
#                 count+= 1
#             queue.extend(node.children.values())
#         return count
    
#     def longest_word(self):
#         if not self.root :
#             return "empty Trie !!!"
        
#         queue = deque([(self.root , "")])
#         long_word = ''
#         while queue:
#             node , word = queue.popleft()
#             if node.end and len(word) > len(long_word):
#                 long_word = word
            
#             for char in sorted(node.children.keys()):
#                 queue.append((node.children[char] , word+char))
#         return long_word
    
#     def list_all_words(self):
#         if not self.root :
#             return []
#         queue = deque([(self.root , "")])
#         words = []
#         while queue:
#             node , word = queue.popleft()
#             if node.end :
#                 words.append(word)

#             for char, child in node.children.items():
#                 queue.append((child , word + char))
#         return words
    
#     def auto_complete(self ,prefix):
#         current = self.root
#         for char in prefix:
#             if char not in current.children:
#                 return []
#             current = current.children[char]
#         queue = deque([(current , prefix)])
#         words = []
#         while queue:
#             node , word = queue.popleft()
#             if node.end:
#                 words.append(word)
#             for char , child in node.children.items():
#                 queue.append((child , word+char))
#         return words
    
# t = Trie()
# t.insertion('anand')
# t.insertion('varun')
# t.insertion('thiru')
# t.insertion('kadir')
# t.insertion('anandkumar')
# t.insertion('arun')
# t.insertion('aathi')
# print(t.search('kadir'))
# print(t.prefix_fuction('ana'))

# print('total number of words :  ',t.count_fuction())
# print('the longest word', t.longest_word())
# print('all words')
# print(t.list_all_words())
# print('all auto complete words')
# print(t.auto_complete('a'))
# print(t.delete('arun'))
# print(t.list_all_words())

# num = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

# val = []
# for i in num:
#     if float('-inf') < i < float('inf'):
#         val.append(i)

# print(val)

# for i in reversed(range(1, 10 )):
#     print(i)
# n = 20

# while n != 0:
#     print(n)
#     n -= 1

# print('end')

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']

# for i , j in zip(questions , answers):
#     print(f'hell {i} and {j}')

# dic = {
#     'name' : 'anand',
#     'class': 10 ,
#     'age': 21
# }

# print(dic['age'])

# for i, (key, value) in enumerate(dic.items()):
#     print(f'Index: {i} - Key: {key} - Value: {value}')

# for i, (key,val) in enumerate(dic.items()):
#     print(f'index is {i} to key {key} - value {val}')

# x= dict(anand = 456 , karthi = 56 , jsdubc =89 ,sbd=90, djsb = 46 , jdsu=34 )
# print(x)

# li = [2,4,5,6,7,8,9]

# out = {x:x*x for x in li}
# print(out)

# dic= {
#     'c':20,
#     'b':30,
#     'a':40
# }

# out = {i+100 for i in dic.values()}
# print(out)

# for k,v in sorted(dic.items()):
#     print(k ,v)

# new_dic = dic.copy()
# new_dic['a'] = 500
# print(new_dic)
# print(dic)

# kk = {'jackkkk': 4098, 'sape': 4139, 'guido': 4127}
# count_len = {}
# for k,v in kk.items():
#     count_len[len(k)] = len(str(v))

# print(count_len)



# name = "dhuraikannu"
# for i in set(name):
#     print(f'{i} is occurred {name.count(i)} times')


# x = 'abracadabra'
# y = 'abrajsybfiyygsabra'
# x = set(x)
# y = set(y)
# print (x - y)
# print (x & y)
# print (x ^ y)
# print (x | y)

# sub = set('abcdgg')
# print(x.issuperset(sub))
# print(sub.issubset(x))

# x = "ndush",
# print(len(x))


# li = [-4 , -4, 9,-6,9,3,-8]
# print('sum', sum(li))

# plus = []
# minus = []
# for i in li:
#     if i < 0:
#         minus.append(-i)
#     else:
#         plus.append(i)

# print(plus)
# print(minus)

# li= [1,3,4]
# li1 = [4,5,7]
# out = []
# for i in li:
#     for j in li1:
#         if i != j:
#             out.append([i,j])
# print(out)

# def fibonassi(n):
#     a,b = 0,1
#     count = 0
#     while a < n:
#         print(a)
#         count = count + a
#         a,b = b,a+b
    
#     print()
#     print('count' , count)
# fibonassi(500)

for i in range(1,6):
    print(f'{i} - {i*i} - {i*i*i}')

x= '770'.zfill(5)
print(x)

# with open('trie.py', 'r') as f:
#     for line in f:
#         print(line ,end="")

with open('DLL.py', 'r') as f:
    for line in f:
        print(line)


