def EffectiveConquer(arr,left,right):
    lindex=0
    rindex=0
    new_arr=[]
    mid=len(left)-1
    end=len(right)-1
    while lindex<=mid and rindex<=end:
        if left[lindex]>right[rindex]:
            new_arr.append(right[rindex])
            rindex=rindex+1;
        else:
            new_arr.append(left[lindex])
            lindex=lindex+1

    while lindex<=mid:
        new_arr.append(left[lindex])
        lindex=lindex+1
    while rindex<=end:
        new_arr.append(right[rindex])
        rindex=rindex+1
    return new_arr


    

def Divide(arr,s,e):
    if(s==e): #base case for loop
        return arr[s:e+1]

    mid=(s+e)//2
    left=Divide(arr, s, mid)
    right=Divide(arr, mid+1, e)
    #Conquer(arr, s, mid, e)
    return EffectiveConquer(arr,left,right)


if __name__ == '__main__':
    test_cases=[[9,2,3,4],
                [4,3,2,1],
                [54,7,33,1,78,90]
                ]
    for case in test_cases:
        print(Divide(case,0,len(case)-1)) #passing array,start,end
