import queue
from collections import deque 

lines = []
maze = []
with open('zad12_demo.txt') as f:
# with open('zad12_input.txt') as f:
	for line in f:
		maze.append([i for i in line.strip("\n")])

for m in maze:
	print(m)

def passable(nr, nc, old_r, old_c, maze):
	if(maze[nr][nc] == maze[old_r][old_c]):
		return True
	elif(ord(maze[nr][nc])-1) == ord(maze[old_r][old_c]):
		return True
	else:
		return False

def solveMaze(maze):
	row, col = len(maze), len(maze[0])

	start = (0, 0)
	for i in range(row):
		for j in range(col):
			if maze[i][j] == 'S':
				start = (i, j)
				break
		else: continue
		break
	else:
		return None

	queue = deque()
	queue.appendleft((start[0], start[1], 0))
	directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
	visited = [[False] * col for _ in range(row)]

	while len(queue) != 0:
		coord = queue.pop()
		visited[coord[0]][coord[1]] = True

		if maze[coord[0]][coord[1]] == "E":
			return coord[2], coord[0],coord[1]


		for dir in directions:
			print(coord[0],coord[1], dir)
			old_r, old_c = coord[0], coord[1]
			nr, nc = coord[0]+dir[0], coord[1]+dir[1]
			# check walls
			if(nr < 0 or nr >= row or nc < 0 or nc >= col):
				print("hit wall")
				continue
			# check if visited the tile or is compatible with rule
			if(visited[nr][nc] and maze[old_r][old_c] != "S" and (not passable(nr, nc, old_r, old_c, maze))):
				print(maze[old_r][old_c],"hit bigger letter")
				continue
			queue.appendleft((nr, nc, coord[2]+1))
			print(queue)

print(solveMaze(maze))