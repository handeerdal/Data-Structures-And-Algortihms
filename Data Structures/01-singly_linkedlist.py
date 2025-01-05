#CREATION OF LINKED LIST

class Node:
    def __init__(self,value=None):
        self.value=value 
        self.next=None
    


class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def append(self, data):#END OF THE LIST
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail=new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.tail=new_node
        self.length+=1

    def prepend(self, data):#BEGGINING OF THE LIST 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length+=1

    def insert(self, index, data): #   sll.insert_after(2, 4) insert 2nd index 4
        """Insert a node after a specific node."""
        current = self.head
        counter=0
        while counter<index-1:
            current = current.next
            counter+=1
        if current is None:
            raise IndexError('index is out of range')
        new_node = Node(data)
        new_node.next=current.next
        current.next=new_node
        self.length+=1
        


    def traverseSLL(self):
        if self.head is None:
            print('there is no list to traverse')
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next


    def searchSLL(self,value):
        if self.head is None:
            print('there is no list to search')
        else:
            node=self.head
            while node is not None:
                if node.value==value:
                    return node.value
                node=node.next

    def get(self,index):
        if self.head is None:
            print('there is no list to get value')
        newnode=self.head
        for i in range (1,index+1):
            if newnode.next==None:
                return 'value does not exist'   
            else:
                newnode=newnode.next
        return newnode.value
            
    def set(self,index,value):
        if self.head is None:
            print('there is no list to set value')
        newnode=self.head
        for i in range (1,index+1):
            if newnode.next==None:
                return 'out of range'   
            else:
                newnode=newnode.next
        newnode.value=value

    def popfirst(self):
            if self.head==None:
                return None
            if self.length==1:
                self.head=None
                self.tail=None

            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            self.length-=1

    def pop(self):
        if self.length == 0:
            print("The list is empty. Nothing to pop.")
            return None
        if self.length == 1:
            popped_node = self.head
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            popped_node = self.tail
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node.value  # Return the value of the popped node
    

    def remove(self,index):
        if index==0:
            self.popfirst()
        elif index==self.length-1:
            self.pop()
        else:
            newnode=self.head
            for _ in range(0,index-1):
                newnode=newnode.next
            popped_element=newnode.next

            newnode.next=popped_element.next
            popped_element=None






            






singlelinkedlist=SlinkedList()
singlelinkedlist.append(0)
singlelinkedlist.append(1)
singlelinkedlist.append(2)
singlelinkedlist.append(3)
singlelinkedlist.insert(2,4)
# singlelinkedlist.traverseSLL()
# print([node.value for node in singlelinkedlist])

# singlelinkedlist.popfirst()
# print([node.value for node in singlelinkedlist])
# singlelinkedlist.pop()
# print([node.value for node in singlelinkedlist])
# print(singlelinkedlist.length)
# singlelinkedlist.traverseSLL()
print([node.value for node in singlelinkedlist])
print(singlelinkedlist.remove(3))
print([node.value for node in singlelinkedlist])
