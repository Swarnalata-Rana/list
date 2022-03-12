def fun():
    a=[1,0,5,8,0,9,3,0,2,0,1,0]
    i=0
    l=[]
    l2=[]
    while i<len(a):
       if a[i]!=0:
           l.append(a[i])
       else:
           l2.append(a[i])
       i=i+1
    l.extend(l2)
    print(l)
fun()