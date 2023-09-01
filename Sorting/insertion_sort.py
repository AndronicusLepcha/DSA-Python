#virtually divede an array in two half sorted and unsorted 

arr=[10,34,2,3,6,15]

for x in range(1,len(arr)):
    curent=arr[x]
    j=x-1
    while(j>=0 and curent<arr[j]):
        arr[j+1]=arr[j]
        j=j-1
    #placement    
    arr[j+1]=curent

print(arr)