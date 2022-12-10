lines, signals = [], []
# with open('zad10_demo.txt') as f:
with open('zad10_input.txt') as f:
	lines = [line.rstrip("\n") for line in f]

cycles, x = 0, 1
pos = []

def append_signals():
	global cycles, x, pos
	pos.append(x)
	if(cycles%40 == 20):
		signals.append(cycles*x)

def oper_cycle(num):
	global cycles, x
	for i in range(2):
		cycles += 1
		append_signals()
		# perfectly adds num to reg on second cycle because i = 1
		x = x + (i * num)

img = []
def draw():
	for j in range(0,6):
		row = ["."]*40
		for i in range(40):
			curr_n = i+j*40
			if(i == (pos[curr_n]-1)):
				row[i] = "#"
			elif(i == pos[curr_n]):
				row[i] = "#"
			elif(i == (pos[curr_n]+1)):
				row[i] = "#"
		img.append(row)

for l in lines:
	if(l.startswith("noop")):
		cycles += 1
		append_signals()
	else:
		oper_cycle(int(l.split()[1]))

draw()

for j in range(len(img)):
	print("".join(img[j]))
# print(signals)
# print(sum(signals))
