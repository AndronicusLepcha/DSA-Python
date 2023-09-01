#select one element from the array and check with all the other element and comapre and update the array

arr=[12,43,67,1,56,2,6,3]

for x in range(0,len(arr)-1):
    smallest=x
    for y in range(x+1,len(arr)):
        print(y)
        if arr[smallest]>arr[y]:
            smallest=y
    temp=arr[smallest]
    arr[smallest]=arr[x]
    arr[x]=temp

print(len(arr))