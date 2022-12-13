import itertools

lines = []
left, right = [], []
with open('zad13_demo.txt') as f:
# with open('zad13_input.txt') as f:
	lines = [line.strip() for line in f]
	for l in lines:
		if(l == ""):
			continue
		if(lines.index(l)%3 == 0):
			left.append(eval(l))
		else:
			right.append(eval(l))

def is_list(elem):
	if(type(elem) == list):
		return elem
	else:
		return list(map(int, str(elem)))

correct_indices = []
def indices(l, r, i):
	print("left: ", l)
	print("right: ", r)
	for el, er in list(itertools.zip_longest(l, r, fillvalue="asdf")):
		if(el == "asdf"):
			print("pair: ", i, "- is in right order - left side shorter")
			return True
		elif(er == "asdf"):
			print("pair: ", i, "- is NOT in right order - right side shorter")
			return False
		if(type(el) == int and type(er) == int):
			if(el < er):
				print("pair: ", i, "- is in right order")
				return True
			# elif(el > er):
			# 	print("pair: ", i, "- is NOT in right order")
			# 	return False
		else:
			indices(is_list(el), is_list(er), i)


i = 1
suma = 0
for l, r in zip(left, right):
	# print(indices(l, r, i))
	if(indices(l, r, i)):
		correct_indices.append(i)
		suma += i
	i += 1


print(correct_indices, suma)
