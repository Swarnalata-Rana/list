list=[1,1,2,3,4,5,1,2]
i=1
a=[]
while i<len(list):
	if list[i] not in a:
		a.append(list[i])
	i+=1
print(a[1:])
#o/p [2,3,4,5]