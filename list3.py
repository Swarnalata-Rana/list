numbers=[80,93,90,70,22,10,7]
i=0
max=0
while i<len(numbers):
	if numbers[i] >max:
		max=numbers[i]
	i=i+1
print("first max=",max)
j=0
smax=0
while j<len(numbers):
	if numbers[j]<max:
		if numbers[j] >smax:
			smax=numbers[j]
		j=j+2
print("second max=",smax)
b=0
tmax=0
while b<len(numbers):
		if numbers[b]<max and numbers[b]<smax:
				if numbers[b]>tmax:
					tmax=numbers[b]
				b=b+3
print("third max=",tmax)
# o/p-fist max=93
# second max=90
# third max=80