#inbuilt function append,pop
# In Python, when you call a local function from within another method of the same class, 
# you typically use self to access that function. This is because self is a reference to the instance of the class, 
# and it allows you to access other instance variables and methods, including local functions.
class Stack:
    def __init__(self):
        self.item=[]

    def push(self,data):
        self.data=data
        self.item.append(self.data)

    def is_empty(self):
        return len(self.item) == 0

    def pop(self):
        if not self.is_empty(): #self is important to call the local function 
            print(self.item.pop())
        else:
            print("Pop from an Empty Stack")

    def peek(self):
        if not self.is_empty():
            print(self.item[-1])
        else:
            print("No item found")

    def display(self):
        if not self.is_empty():
            for x in self.item:
                print(x)
        else:
            print("No item Available")

s = Stack()
s.display()
s.pop()
s.push(123)
s.push(34)
s.push(19)
s.display()
s.peek()
s.pop()
s.pop()
s.pop()
s.pop()
