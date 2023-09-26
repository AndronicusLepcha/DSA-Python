def conquer(arr,l,mid,h):
    indx1=l
    indx2=mid+1
    merge=[]
    i=0
    while indx1<=mid and indx2<=h:
        if arr[indx1]<arr[indx2]:
            merge.append(arr[indx1])
            indx1=indx1+1
        else:
            merge.append(arr[indx2])
            indx2=indx2+1
    while indx1<=mid:
        merge.append(arr[indx1])
        indx1=indx1+1
    while indx2<=h:
        merge.append(arr[indx2])
        indx2=indx2+1

    for x in range(l,h+1):
        arr[x]=merge[i]
        i=i+1

def mergesort(arr,l,h):
    if l==h:
        return arr
    mid=(l+h)//2

    mergesort(arr, l, mid)
    mergesort(arr, mid+1, h)
    conquer(arr,l,mid,h)



arr=[23,21,20,4,15,6];
mergesort(arr,0,len(arr)-1)
print(arr)