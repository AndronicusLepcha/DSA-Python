# str = baccad ans=bccd
def RemoveA(str,length,i):
    if length==i:
        return ""

    result=str[i]

    if result=='a':
        return RemoveA(str, length, i+1)
    else:
        return result+RemoveA(str, length, i+1)

str="bacsacad"
print(RemoveA(str,len(str),0))

