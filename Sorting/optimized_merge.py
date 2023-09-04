def mergesort(arr):
    if len(arr)<=1:
        return 

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    mergesort(left)
    mergesort(right)
    merge(left,right,arr)

def merge(l,r,arr):
    k=idx1=idx2=0
    len_a=len(l)
    len_b=len(r)
    #out=[]
    while idx1 < len_a and idx2 < len_b:
        if l[idx1]<=r[idx2]:
            #out.append(l[idx1])
            arr[k]=l[idx1]
            idx1 = idx1+1

        else:
            #out.append(r[idx2])
            arr[k]=r[idx2]
            idx2 = idx2+1
        
        k=k+1

    while idx1<len_a:
        #out.append(l[idx1])
        arr[k]=l[idx1]
        idx1=idx1+1  
        k=k+1   

    while idx2<len_b:
        #out.append(r[idx2])
        arr[k]=r[idx2]
        idx2=idx2+1
        k=k+1




# arr1=[45,56,67]
# arr2=[23,43,66]
# out=merge(arr1,arr2)
arr=[112,33,45,6,2,8,90]

mergesort(arr)
print(arr)    

