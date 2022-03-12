a=[1,2,2,5,8,4,4,]
i=0
c=[]
while i<len(a):
	if a[i] not in c:
		c.append(a[i])
	i+=1
print(c)
#o/p [1,2,5,8,4]