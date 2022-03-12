a=[5,6,[],3,[],[],9]
i=0
b=[]
c=[]
while i<len(a):
	if a[i]==b:
		pass
	else:
		c.append(a[i])
	i+=1
print(c)
# o/p-[5,6,3,9]