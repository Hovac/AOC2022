with open('zad3.txt') as f:
	lines = [line.rstrip() for line in f]

split1 = []
split2 = []
p1 = []
p2 = []
p3 = []

# for l in lines:
# 	s1 = slice(0, len(l)//2)
# 	s2 = slice(len(l)//2, len(l))
# 	split1.append(l[s1])
# 	split2.append(l[s2])

i = 0
for l in lines:
	i +=1
	print(i, l)
	if i == 1:
		p1.append(l)
	elif i == 2:
		p2.append(l)
	if i == 3:
		p3.append(l)
		i = 0

def sCompare(s1, s2):
	for i in s1:
		if i in s2:
			if(i.isupper()):
				return ord(i)-38
			else:
				return ord(i)-96
	return 0

def sBadge(s1, s2, s3):
	tempS = ''.join(set(s1).intersection(s2))
	return (''.join(set(tempS).intersection(s3)))

dupl = []

for (a, b, c) in zip(p1, p2, p3):
	dupl.append(sBadge(a, b, c))

sum = 0
for lt in dupl:
	print(lt)
	if(lt.isupper()):
		sum += ord(lt)-38
	else:
		sum += ord(lt)-96
print(sum)
# sum = 0
# for a, b in zip(split1, split2):
# 	sum += sCompare(a, b)

# print(sum)
