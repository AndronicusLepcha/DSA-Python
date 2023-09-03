from collections import deque

class Stock:
    def __init__(self):
        self.buffer=deque()
    
    def insert(self,data):
        self.buffer.appendleft(data)
    
    def is_empty(self):
        return len(self.buffer) == 0

    def delete(self):
        if not self.is_empty():
            print(self.buffer.pop())
        else:
            print("Empty Queue")
    
    def show(self):
        if not self.is_empty():
            print(list(self.buffer))
        else:
            print("Empty Queue")
s=Stock()
s.show()
s.insert({'Time':'12:0','Zil Price':'200.11'})
s.insert({'Time':'12:10','BitCoin Price':'2450.11'})
s.delete()
s.delete()
s.delete()
s.delete()