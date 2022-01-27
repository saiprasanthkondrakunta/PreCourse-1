class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
       self.list1 = []
         
     def isEmpty(self):
       return self.list1 == []
        
         
     def push(self, item):
       self.list1.insert(0,item)

         
     def pop(self):
       self.list1.pop(0)
        
        
     def peek(self):
       return self.list1[0]
        
     def size(self):
       return len(self.list1)
         
     def show(self):
       return self.list1
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
