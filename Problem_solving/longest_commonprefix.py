
def longestCommonPrefix(strs):
        s=''
        count=0
        for i in strs[0]:
            r=1
            for j in strs:
                if len(j)-1<count or i!=j[count]:
                    r=0
                    break
            if r==0:
                break
            else:
                count+=1
                s=s+i
        return s

str=["flower","flow","flight"];
print(longestCommonPrefix(str))