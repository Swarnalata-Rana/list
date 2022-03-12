list=[2,-7,5,-64,-14]
i=0
a=0
b=0
while i<len(list):
	if list[i]>0:
		b+=1
	else:
		a+=1
	i+=1
print(a)
print(b)
# o/p-negative number 3
# positive number 2