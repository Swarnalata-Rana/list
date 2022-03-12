list=[1,2,3,4,5,6,7,8,9,10]
i=1
a=[]
while i<len(list):
	c=list[-i]-list[-i-1]
	a.append(c)
	i+=1
print(a)
# o/p-[1,1,1,1,1,1,1,1,1]