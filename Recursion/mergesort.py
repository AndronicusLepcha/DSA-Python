def Conquer(arr,s,mid,e):
    mixarray=[] #Empty list to store array
    id1=s   #This is to point at the first array returned
    id2=mid+1   #This is to point second array returned
    

    while id1<=mid and id2<=e:
        if arr[id1]<arr[id2]:  # if element in first array is less than the second array then append in mixarray
            mixarray.append(arr[id1])
            id1=id1+1
        else:   #swap element of second array that is smaller than the first array
            mixarray.append(arr[id2])
            id2=id2+1
        
    # The array size of the two array returned may not be of same so if it is not same then append all the rest array
    while id1<=mid:
        mixarray.append(arr[id1])
        id1=id1+1
    while id2<=e:
        mixarray.append(arr[id2])
        id2=id2+1
    #now append those mixed array into the original array
    for x in range(0,len(mixarray)):
        arr[s+x]=mixarray[x]

def Divide(arr,s,e):
    if(s==e): #base case for loop
        return

    mid=(s+e)//2
    Divide(arr, s, mid)
    Divide(arr, mid+1, e)
    Conquer(arr,s,mid,e)

if __name__ == '__main__':
    test_cases=[[1,2,3,4],
                [4,3,2,1],
                [54,7,33,1,78,90]
                ]
    for case in test_cases:
        Divide(case,0,len(case)-1) #passing array,start,end
        print(case)
