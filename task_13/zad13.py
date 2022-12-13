import functools as ft

lines = []
left, right, signals = [], [], []
# with open('zad13_demo.txt') as f:
with open('zad13_input.txt') as f:
	lines = [line.strip() for line in f]
	for l in lines:
		if(l == ""):
			continue
		signals.append(eval(l))
		if(lines.index(l)%3 == 0):
			left.append(eval(l))
		else:
			right.append(eval(l))

def is_list(elem):
	if(type(elem) == list):
		return elem
	else:
		return [elem]

correct_indices = []
def indices(l, r):
		if(type(l) == int and type(r) == int):
			return (l < r) - (r < l)
		elif(type(l) == list and type(r) == list):
			for i in range(min(len(l), len(r))):
				j = indices(l[i], r[i])
				if(j != 0):
					return j
			return indices(len(l), len(r))
		else:
			l = is_list(l)
			r = is_list(r)
			return indices(l, r)

i = 1
for l, r in zip(left, right):
	if(indices(l, r) > 0):
		correct_indices.append(i)
	i += 1

print(correct_indices, sum(correct_indices))

signals.append([[2]])
signals.append([[6]])
signals.sort(key= ft.cmp_to_key(indices))
signals = signals[::-1]
product = 1
for index, s in enumerate(signals):
	if(s == [[2]] or s == [[6]]):
		product *= (index+1)
		print(index+1, s)
print(product)
