#Bubble Sort

arr=[10,3,12,4,8,1,2,78]

for i in range(0,len(arr)-1):
    for y in range(i+1,len(arr)-1):
        if arr[i]>arr[y]:
            temp=arr[i]
            arr[i]=arr[y]
            arr[y]=temp
print(arr)


#time compleixty is O(n^2)