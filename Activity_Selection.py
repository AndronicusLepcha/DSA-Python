index=[1,2,3,4,5,6]
p=[200,180,190,300,120,100]
dl=[5,3,3,2,4,2]
pf=0

for i in range(len(index)):
    
    for j in range(len(index)):
        if p[i]>p[j]:
            p[i],p[j]=p[j],p[i]
            index[i],index[j]=index[j],index[i]
            dl[i],dl[j]=dl[j],dl[i]
            
sv=[0,0,0,0,0]
for i in range(max(dl)):
    cur=dl[i]-1
    if sv[cur]==0:
        sv[cur]=index[i]
        pf=pf+p[i]
        

    else:
        for j in range(cur,-1,-1):
            if sv[j]==0:
                sv[j]=index[i]
                pf=pf+p[i]
print(sv)
print(pf)