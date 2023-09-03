from collections import deque
q = deque()

def insert(data):
    idata=q.appendleft(data)
    print("Inserted Data: ",data)

def delete():
    d=q.pop()
    print("Deleted Item: ",d)

def display():
    for x in q:
        print("Elements present in Queue: ",x)
    print(list(q))


insert(100)
insert(300)
insert(99)
insert(200)
insert(80)
delete()
display()
delete()
display()