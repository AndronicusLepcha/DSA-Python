def count(arr):
    ct=0
    for x in range(0,len(arr)-1):
        if arr[x] > arr[x+1]:
            start=arr[x]
            i=x+1
            while start > arr[i]:
                ct = ct+(start-arr[i])
                i=i+1
                if start>arr[i] and i==len(arr)-1:
                    ct=0
                    print("Array is in Descending order ")
                    break
            break
    return ct
    #TEST Cases
arr=[[3,2,2,1,2,4,5],
        [1,2,3,4,5],
        [4,3,2,1],
        [3,2,11],
        [3,2,1,4,5]]

        
for x in arr:
    print(count(x))