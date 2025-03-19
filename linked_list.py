class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertatbegin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insertatlast(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next

        last.next=new_node


    def insertatindex(self ,index,data):
        new_node=Node(data)
        if (index==0):
            self.insertatbegin(data)

        current=self.head
        for i in range(index-1):
            current=current.next
        
        if current != None:
            new_node.next=current.next
            current.next=new_node
    


    def updatevalue(self,index,new_data):
        current=self.head
        for i in range(index):
            if current!=None:
                current=current.next
            
        
        if current != None:
            current.data=new_data
        else:
            print('incorect index!')

        
    def removeatbiginig(self):
        if self.head == None:
            print('linked list is empty!')
        removed_data=self.head.data
        self.head=self.head.next
        print(f'successfully removed first {removed_data} data!')

    
    def removelast(self):
        if self.head == None:
            print('linked list is empty!')
            return

        current=self.head

        while current.next and current.next.next:
            current=current.next
        remoed_data=current.next.data
        current.next=None

        print(f'successfully removed last {remoed_data} data!')

    
    def removeatindex(self,index):
        if self.head ==None:
            print('empty!')
        
        if index==0:
            self.removeatbiginig(index)
        current=self.head

        for i in range(index-1):
            if current ==None:
                print('INvalid idex!')
            current=current.next

        if current is None:
            print('Invaild Index!')
        remoed=current.data
        current.next=current.next.next
        print(f'successfully removed {index} index in {remoed} data!')



    def removeelement(self,target):
        if self.head ==None:
            print('empty!')

        current=self.head
        previous=None

        while current and current.data !=target:
            previous=current
            current=current.next

        if current is None:
            print('emplty')
        removed=current.data
        previous.next=current.next
        print(f'successfully removed {target}  in {removed} data!')




    def sizeoflist(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
    
        return count


       
    def printlist(self):
        current=self.head
        while current:
            print(current.data , end='-->')
            current=current.next
            
        print('End!')

    
li=LinkedList()
li.insertatbegin(10)
li.insertatbegin(90)
li.insertatbegin(870)

li.insertatlast(20)
li.insertatlast(890)
li.insertatlast(560)

li.insertatindex(1,89)
li.insertatindex(3,9909)
li.insertatindex(4,54)
li.insertatindex(2,32)

li.updatevalue(1,1000)

li.removeatbiginig()
li.removelast()
li.removeatindex(3)
li.removeatindex(2)
li.removeelement(890)


size=li.sizeoflist()
print('total:',size)
li.printlist()