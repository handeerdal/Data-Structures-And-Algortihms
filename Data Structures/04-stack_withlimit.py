class Stack():
    def __init__(self,maxsize):
        self.list=[] 
        self.maxsize=maxsize
    def __str__(self):
        vals= [str(values) for values in reversed(self.list)]
        return ' '.join(vals)
    def isEmpty(self):
        if len(self.list)==0:
            return 0
        else:
            1
    def isFull(self):
        if len(self.list)==self.maxsize:
            return 1
        else:
            return 0
    def push(self,val):
        if self.isFull():
            print('it is full')
        else:
            self.list.append(val)

    
newstack=Stack(5)
newstack.push(1)
newstack.push(1)
newstack.push(1)
newstack.push(1)
newstack.push(1)
newstack.push(1)
newstack.push(1)
print(newstack)

