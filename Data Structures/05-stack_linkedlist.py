class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None
    

class LList():
    def __init__(self):
        self.top=None
    def __iter__(self):
        cur=self.top
        while cur:
            yield cur
            cur=cur.next



class Stack():
    def __init__(self):
        self.LList=LList()

    def __str__(self):
        vals=[str(value.val) for value in self.LList]
        return ' '.join(vals)
    def IsEmpty(self):
        if self.LList.top==None:
            return 1
        else:
            return 0
    def push(self,val): #it is reversed
            if self.IsEmpty():
                print( 'list is empty')
            else:
                newnode=Node(val)
                newnode.next=self.LList.top
                self.LList.top=newnode
    def pop(self):
        if self.IsEmpty():
            print( 'list is empty')
        else:
            removed= self.LList.top.val
            self.LList.top=self.LList.top.next
            print(f'{removed} is removed')
    def peek(self):
         if self.IsEmpty():
                print( 'list is empty')
         else:
             return(self.LList.top.val)
    def delete(self):
         self.LList.top=None
         

         

stack=Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()

print(stack)
print(stack.IsEmpty())