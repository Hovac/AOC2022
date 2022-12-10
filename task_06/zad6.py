lines = []
with open('zad6.txt') as f:
	lines = [line.rstrip("\n") for line in f]

def check_dupls(listElements):
    if len(listElements) == len(set(listElements)):
        return False
    else:
        return True

first = 0

def firstOccy(lin):
	for i in range(len(lin)-13):
		tArr = []
		for j in range(14):
			tArr.append(l[j+i])
		if(not check_dupls(tArr)):
			return i + 14

for l in lines:
	print(firstOccy(l))


