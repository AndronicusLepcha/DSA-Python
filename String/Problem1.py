# Find the character in a string whose frequency is second largest
w="warrrrthhwworldd"
freq=[]
ch=[]
count =0 
for char in w:
    if char not in ch:
        ch.append(char)
        for c in w:
            if char==c:
                count=count+1
        freq.append(count)
        count = 0
print("String=",ch)
print("Frequency=",freq)    

mx=temp=0
for x in range(0,len(freq)):
    if freq[x]>freq[mx]:
        temp=mx
        mx=x

print("string whose frequency is  Second highest is ",w[temp])
