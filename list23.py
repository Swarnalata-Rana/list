def fun():
    a=["runu","laxmi","abhipsha"]
    i=0
    while i<len(a):
        j=0
        c=0
        while j<len(a[i]):
            c=c+1
            j=j+1
        print(a[i],c)
        i=i+1
fun()
# o/p-runu 4
#     laxmi 5
# abhipsha 8