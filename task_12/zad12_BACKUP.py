import queue

lines = []
with open('zad12_demo.txt') as f:
# with open('zad12_input.txt') as f:
	lines = [line.strip() for line in f]

maze = []
for l in lines:
	row = []
	for s in l:
		row.append(s)
	maze.append(row)

for m in maze:
	print(m)

def start_pos(maze):
	for i in range(len(maze)):
		for x, pos in enumerate(maze[i]):
			if pos == "S":
				return x, i

def controls(cmd):
	if cmd == "L":
		return [-1, 0]
	elif cmd == "R":
		return [1, 0]
	elif cmd == "U":
		return [0, -1]
	elif cmd == "D":
		return [0, 1]

def valid_move(maze, moves):
	startx, starty = start_pos(maze)
	i = startx
	j = starty
	for move in moves:
		t_i, t_j = i, j
		dx, dy = controls(move)
		i += dx
		j += dy

		# check for walls
		if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
			# print("hit wall", maze[j][i], i, j)
			return False
		elif ((ord(maze[j][i])-1) == ord(maze[t_j][t_i])):
			print(maze[t_j][t_i], maze[j][i], j, i)
			print(ord(maze[t_j][t_i]), ord(maze[j][i]), j, i)
			return False
	return True


def findEnd(maze, moves):
	startx, starty = start_pos(maze)

	i = startx
	j = starty
	for move in moves:
		dx, dy = controls(move)
		i += dx
		j += dy
		# print(maze[j][i], j, i)
	
	if maze[j][i] == "E":
		print("End found in ", len(moves), " moves")
		return True
	
	return False

nums = queue.Queue()
nums.put("")
add = ""
while not findEnd(maze, add):
	add = nums.get()
	print(add)
	for i in ["U", "D", "L", "R"]:
		put = add + i
		if valid_move(maze, put):
			nums.put(put)
