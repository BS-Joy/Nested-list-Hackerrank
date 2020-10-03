n = int(input())
theList = []
mark = []
for i in range(n):
	a = []
	for j in range(2):
		if j == 0:
			a.append(input())
		else:
			x = float(input())
			a.append(x)
			mark.append(x)
	theList.append(a)

print()
theList.sort()
mark.sort()

for i in range(n):
	if mark[1] == theList[i][1]:
		print(theList[i][0])

