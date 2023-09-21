def FindPivot(arr,low,high):

    pivot=arr[high]
    i=low-1 #points to 1-starting of the array index so lesser element are added first  

    for x in range(low,high):
        if pivot>arr[x]:
            i = i+1
            arr[i],arr[x]=arr[x],arr[i]

    i=i+1;
    arr[i],arr[high]=arr[high],arr[i]
          
    return i

def QuickSort(arr,low,high):
    if low < high:
        pivot=FindPivot(arr,low,high)
        QuickSort(arr, low, pivot-1)
        QuickSort(arr, pivot+1, high)


arr=[[7,3,2,1,8,4],
    [1,2,3,4,5],
    [5,4,3,2,1]]
for a in arr:
    QuickSort(a,0,len(a)-1)
    print(a)