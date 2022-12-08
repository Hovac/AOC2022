with open('zad4.txt') as f:
	lines = [line.rstrip() for line in f]

pair1 = []
pair2 = []

for l in lines:
	tempL = l.split(',')
	pair1.append(tempL[0])
	pair2.append(tempL[1])

pi1 = []
pi2 = []

for (p1, p2) in zip(pair1, pair2):
	tNum1 = p1.split('-')
	tempi1 = []
	for i in range(int(tNum1[1]) - int(tNum1[0]) + 1):
		tempi1.append(int(tNum1[0]) + i)
	pi1.append(tempi1)

	tNum2 = p2.split('-')
	tempi2 = []
	for i in range(int(tNum2[1]) - int(tNum2[0]) + 1):
		tempi2.append(int(tNum2[0]) + i)
	pi2.append(tempi2)

sum = 0
# for (p1, p2) in zip(pi1, pi2):
# 	if(set(p1).issubset(set(p2))):
# 		print("p1 is subset of p2", p1, p2)
# 		sum += 1 
# 	elif(set(p2).issubset(set(p1))):
# 		print("p2 is subset of p1", p1, p2)
# 		sum += 1 

for (p1, p2) in zip(pi1, pi2):
	if(not set(p1).isdisjoint(p2)):
		sum += 1

print(sum)


