class Stack():
   def __init__(self):
        self.list=[] 
   def __str__(self):
      vals= [str(values) for values in reversed(self.list)]
      return ' '.join(vals)
      
   def push(self,val):
       self.list.append(val)
   def pop(self):
       self.list.pop()
   def peek(self):
       return self.list[-1]
   def delete(self):
       self.list=[]
   def isEmpty(self):
       if len(self.list)==0:
           return 0
       else:
           return 1



mystack=Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
print(mystack)
print(mystack.peek())