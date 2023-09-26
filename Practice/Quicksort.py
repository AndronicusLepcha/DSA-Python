
def partition(arr,l,h):
    pivot=arr[h]
    j=l-1
    for i in range(l,h):
        if pivot>arr[i]:
            j=j+1
            arr[j],arr[i]=arr[i],arr[j]
    j=j+1
    arr[j],arr[h]=pivot,arr[j];
    return j

def divide(arr,l,h):
    if l>h:
        return;
    pivot=partition(arr,l,h)
    divide(arr,pivot+1,h)
    divide(arr, l, pivot-1)
    

arr=[4,2,9,1,8,3]
divide(arr,0,len(arr)-1);
print(arr)