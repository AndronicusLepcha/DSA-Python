#implementing linear search
#time complexity O(n)

list=[101,22,3,4,5,6,67,23]
key=int(input('Enterthe key element to find '))
for x in list:
    if x == key:
        print('Element found at index ',list.index(x))


#or

def linear(arr,key):
    for x in arr:
        if x == key:
            return arr.index(x)
    return -1
arr=[12,33,44,224,76,887,33,222,66,98,9809,34,56]
key=int(input('Enter the key to find '))

v=linear(arr,key) #calling linear function by passing array and key 

if(v == -1):
    print('element not found')
else:
    print('element prsent at index {}'.format(v))