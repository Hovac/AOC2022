lines, comms, moves = [], [], []
with open('zad9_input.txt') as f:
	lines = [line.rstrip("\n") for line in f]
	for l in lines:
		comms.append(l.split(" ")[0])
		moves.append(int(l.split(" ")[1]))

command = {
	"U": (0, 1),
	"D": (0, -1),
	"L": (-1, 0),
	"R": (1, 0),
}

#        x, y
head = 	[0, 0]
tail = 	[0, 0]
rope = [[0, 0] for i in range(10)]

# get sign by which to change position
sign = lambda x : 1 if x > 0 else (-1 if x < 0 else 0)
def check_tail():
	global head, tail
	dx = head[0] - tail[0] 
	dy = head[1] - tail[1]
	# solve rows/columns
	if(dx == 0 or dy == 0):
		if(abs(dx) >= 2):
			tail[0] += sign(dx)
		if(abs(dy) >= 2):
			tail[1] += sign(dy)
	# solve diagonal
	elif((abs(dx), abs(dy)) != (1, 1)):
		tail[0] += sign(dx)
		tail[1] += sign(dy)

def check_rope(i):
	global rope
	#	 first segment - second segment
	dx = rope[i-1][0] - rope[i][0] 
	dy = rope[i-1][1] - rope[i][1]
	# solve rows/columns
	if(dx == 0 or dy == 0):
		if(abs(dx) >= 2):
			rope[i][0] += sign(dx)
		if(abs(dy) >= 2):
			rope[i][1] += sign(dy)
	# solve diagonal
	elif((abs(dx), abs(dy)) != (1, 1)):
		rope[i][0] += sign(dx)
		rope[i][1] += sign(dy)


# fun hack, set doesn't add same elements twice, it replaces current one - NOICE
move_counter = set()

# print(" HEAD   TAIL  command")
for c, m in zip(comms, moves):
	for i in range(m):
		dx, dy = command[c]
		rope[0][0] += dx
		rope[0][1] += dy
		# check_tail()
		for i in range(1, 10):
			check_rope(i)
		# move_counter.add((tail[0], tail[1]))
		move_counter.add(tuple(rope[-1]))

print(len(move_counter))