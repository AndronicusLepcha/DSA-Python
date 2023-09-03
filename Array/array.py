arr=[1,2,3,4]
print(arr)
print(id(arr)) # location of the object arr
arr.append(45)

#printing an array
#print(arr)
#or
for x in arr:
    print(x)

#searching is O(n) 
key=4
for x in arr:
    if x==key:
        print("Element Found")
        break
    else:
        continue #skip this iteration

#insertion is O(n)
arr.insert(1,99) # add 99 to index 1 and shift the other element