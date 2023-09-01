def partition(arr,low,high):
    pivot =arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

    i=i+1
    temp=arr[i]
    arr[i]=pivot
    arr[high]=temp
    print(arr)
    return i
        



def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr=[6,3,9,5,10,8] 
low=0
high=len(arr)-1

quicksort(arr,low,high)
print(arr)