class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# class SingleLinkedList:
#     def __init__(self):
#         self.head = None
        
#     def insertatbegin(self , data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insertatend(self ,data ):
#         new_node = Node(data)
#         if self.head is None:
#             return self.insertatbegin(data)
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
        
#     def deleteatbegin(self):
#         if self.head is not None:
#             self.head = self.head.next
        
#     def deleteatend(self):
#         current = self.head
#         prve = None
#         while current.next:
#             prve = current
#             current = current.next
#         prve.next = None

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end="->")
#             current = current.next
#         print("end!")

#     def counting(self):
#         curent = self.head
#         count = 0
#         while curent:
#             count += 1
#             curent = curent.next
#         return count
    
#     def reverce(self):
#         current = self.head
#         prev = None
#         while current:
#             new_node = current.next
#             current.next = prev
#             prev = current
#             current = new_node
#         self.head= prev 
        

        


# s1 = SingleLinkedList()
# s1.insertatbegin(20)
# s1.insertatbegin(30)
# s1.insertatbegin(40)
# s1.insertatbegin(50)
# s1.insertatbegin(60)
# s1.display()
        
# s1.deleteatbegin()
# print(f'after delete begin {s1.display()}') 
# s1.deleteatend()
# print(f'after delete end {s1.display()}') 
        
# print("Number of nodes:", s1.counting())  
# s1.reverce()
# s1.display()
        
        

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DLL:
#     def __init__(self):
#         self.head = None

#     def addatbegin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         new_node.next = self.head
#         self.head.prev = new_node  # Set previous of existing head to new node
#         self.head = new_node  # Update head to new node
        
#     def addatend(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
            
#         current = self.head
#         while current.next:
#             current = current.next
            
#         current.next = new_node
#         new_node.prev = current  # Set previous of new node to current
        
#     def deleteatbegin(self):
#         if self.head is None:
#             return
            
#         if self.head.next:
#             self.head = self.head.next
#             self.head.prev = None  # Update previous of new head to None
#         else:
#             self.head = None

#     def deleteatend(self):
#         if self.head is None:
#             return
            
#         if self.head.next is None:
#             self.head = None
#             return
            
#         current = self.head
#         while current.next:
#             current = current.next
            
#         current.prev.next = None  # Set next of second-to-last node to None

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end="<-->")
#             current = current.next
#         print('end!')

#     def printBackward(self):
#         current = self.head
#         while current.next:
#             current = current.next
#         while current:
#             print(current.data , end="<--")
#             current  = current.prev
#         print('start')
    

        

# # Create a DLL instance and test it
# d1 = DLL()  # Don't pass any arguments here
# d1.addatbegin(10)
# d1.addatend(20)
# d1.addatend(30)
# d1.addatend(40)
# d1.display()

# d1.deleteatbegin()
# d1.display()
# d1.deleteatend()
# d1.addatend(30)
# d1.addatend(40)
# print('backword:')
# d1.printBackward()
# d1.display()
        
        
        
        
class CircularList:
    def __init__(self) -> None:
        self.head = None

    def addtobegin(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def addtoend(self , data):
        new_node = Node(data)

        if self.head is None:
            self.addtobegin(data)
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node = current

    def deleteatbegin(self ):
        if self.head is None:
            print("empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
    def deleteatend(self):
        if self.head is None:
            print("empty")
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next

        prev.next = self.head


    def display(self):
        current  = self.head
        while current.next != self.head:
            print(current.data , end='-->')
            current = current.next
        print('now point to head')

    def counting(self):
        current = self.head
        count = 1
        while current.next!= self.head:
            count +=1
            current = current.next
        return count


c1 =CircularList()
c1.addtobegin(10)
c1.addtobegin(20)
c1.addtobegin(40)
c1.addtobegin(60)
c1.addtobegin(70)
c1.addtobegin(240)
c1.addtobegin(108)
c1.addtobegin(200)
c1.display()
c1.deleteatbegin()
c1.display()
c1.deleteatend()
c1.display()
print(f"Total nodes: {c1.counting()}")
        
            