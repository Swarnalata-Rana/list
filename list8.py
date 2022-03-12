list=[4,6,4,3,3,4,3,4,3,8]
a=2
b=[]
while a<len(list):
	if list[a]not in b:
		b.append(list[a])
	a+=1
print(b)
# o/p-[4,3,8]