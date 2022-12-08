lines = []
with open('zad8.txt') as f:
	lines = [line.rstrip("\n") for line in f]

cols = []

for l in lines:
	rows = []
	for s in l:
		rows.append(int(s))
	cols.append(rows)
	rows = []

vis_trees = (len(cols)*4)-4

def check_higher(m, n , patch):
	global vis_trees
	node = patch[m][n]
	transposed_patch = list(zip(*patch))
	# check sides
	if(node <= max(patch[m][:n]) and node <= max(patch[m][n+1:]) and node <= max(transposed_patch[n][:m]) and node <= max(transposed_patch[n][m+1:])):
		return
	else:
		vis_trees += 1

def scene(m, n , patch):
	r, l, t, b = 0, 0, 0, 0
	node = patch[m][n]
	left_side = patch[m][:n]
	if(len(left_side) > 1):
		left_side.reverse()
	print("node: ", node, m, n)
	for left in left_side:
		l += 1
		if node <= left:
			break
	right_side = patch[m][n+1:]
	for right in right_side:
		r += 1
		if node <= right:
			break
	transposed_patch = list(zip(*patch))
	top_side = []
	top_side = list(transposed_patch[n][:m])
	if(len(top_side) > 1):
		top_side = top_side[::-1]
	for top in top_side:
		t += 1
		if node <= top:
			break
	# print(top_side, t)
	bot_side = transposed_patch[n][m+1:]
	for bot in bot_side:
		b += 1
		if node <= bot:
			break
	return (r * l * t * b)

scores = []

for i in range(1, len(cols)-1):
	for j in range(1, len(cols[i])-1):
		# check_higher(i, j, cols)
		scores.append(scene(i, j, cols))

print(scores)

print(max(scores))