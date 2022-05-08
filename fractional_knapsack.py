"""ALgorith
for i=1 to n
    if weight+w[i]<=W
      then clo[i]=1 or 0
     else 
       col[i]=(W-weight)/w[i]
       weight=W[i]*col[i]+weight
       break
"""

index=[1,2,3,4]
p=[50,70,20,45]
w=[40,20,10,15]
clo=[1,1,1,1]
weight=0
W=65
pf=0

for i in range(len(index)):
    
    for j in range(len(index)):
        if p[i]>p[j]:
            p[i],p[j]=p[j],p[i]
            index[i],index[j]=index[j],index[i]
            w[i],w[j]=w[j],w[i]
            
            """ profit=[105, 70, 50, 20]
                index=[4, 2, 1, 3]
                weight=[15, 20, 40, 10]"""
            
for j in range(len(index)):
    if weight+w[j]<=W:
        clo[j]=0
        weight=weight+w[j]
        pf=pf+p[j]
    else:
        clo[j]=(W-weight)/w[j]
        weight=clo[j]*w[j]+weight
        pf=pf+p[j]*clo[j]
        break
print(clo)
print(pf)
