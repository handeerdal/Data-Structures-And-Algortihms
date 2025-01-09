class Node():
    def __init__(self,value=0):
        self.value=value
        self.next=None
class CSLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    def __str__(self):
        tempnode=self.head
        result=''
        while tempnode is not None:
            result+=str(tempnode.value)
            tempnode=tempnode.next
            if tempnode==self.head:
                break
            result+='->'
        return result
    def append(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            newnode.next=newnode
        else:
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
    
    def prepend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            newnode.next=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=newnode
    def insert(self,value,place):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            newnode.next=newnode
        elif place==0:
            self.prepend(value)
        else:
            count=0
            curr=self.head
            while count!=(place-1):
                curr=curr.next
                count+=1
            if curr.next==self.head:
                self.append(value)
            else:
                newnode.next=curr.next
                curr.next=newnode
    def popfirst(self):
        if self.head==None:
            return None
        popped=self.head
        self.head=self.next
        self.tail.next=self.head
        popped.next=None
        
    def pop(self):
        if self.head==None:
            return None
        popped=self.tail
        temp=self.head
        while temp.next is not self.head:
            temp=temp.next
        temp.next=self.head
        self.tail=temp
        popped.next=None
    def remove(self,val):
        if self.head==None:
            return None
        temp=self.head
        while temp.next!=self.head:
            if temp.value==val:
                self.head=temp.next
                self.tail.next=temp.next
                break


            if temp.next==self.head:
                print('value not found')
                break
            if temp.next.value==val:
                popped=temp.next
                temp.next=temp.next.next
                popped.next=None
                break
            else:
                temp=temp.next
            



        


cslist=CSLinkedList()
cslist.append(10)
cslist.append(20)
cslist.append(30)
cslist.insert(40,2)
cslist.prepend(50)
cslist.insert(60,0)
cslist.insert(70,1)
cslist.insert(90,7)
cslist.remove(90)
print(cslist.head)
print(cslist)


            


     