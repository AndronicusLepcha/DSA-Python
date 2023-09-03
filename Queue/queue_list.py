#my_list = [1, 2, 3]
# my_list.insert(0, 4)  # Insert 4 at index 0
# Result: [4, 1, 2, 3]

#operation 
#1.Insertion
#2.Deletion
#3.Print

class Queue:
    def __init__(self):
        self.list=[]
    
    def insert_in_queue(self,data):
        self.list.insert(0,data)

    def delete_in_queue(self):
        print("Deleted Element: ",self.list.pop())
    
    def show_queue(self):
        for x in self.list:
            print("Element : ",x)

q=Queue()
n=int(input("Enter the n number you want to add in queue"))
for x in range(0,n):
    data=int(input("Enter your data: "))
    q.insert_in_queue(data)

q.delete_in_queue()
q.show_queue()
