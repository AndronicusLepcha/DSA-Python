arr=[3,5,7,8,11,30,88]
si=0
ei=len(arr)-1

key=int(input('Enter the Key'))
while(si<=ei):
    mid=(si+ei)//2
    if arr[mid]==key:
        print('Key found at index ',mid)
        break
    elif key>mid:
        si=mid+1
    else:
        ei=mid-1