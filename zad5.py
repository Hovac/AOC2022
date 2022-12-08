import re

lines = []
with open('zad5.txt') as f:
	lines = [line.rstrip("\n") for line in f]

def parseStacks(ls):
	cells = []
	regex = "[a-zA-Z]+"
	for l in ls:
		if 'move' in l:
			break
		rows = []
		i = 0
		for s in l:
			tStr = ""
			if(s == " "):
				if(i%4 == 1):
					tStr = "0"
					rows.append(tStr)
			elif re.match(regex, s):
				tStr = s
				rows.append(tStr)
			i += 1
		cells.append(rows)
	cells.pop()
	cells.pop()
	tcells = list(map(list,zip(*cells)))
	for tc in tcells:
		while '0' in tc:
			tc.remove('0')
	return tcells

def parseCommand(ls):
	comms = []
	for l in ls:
		if 'move' in l:
			comms.append(re.findall(r'\d+', l))
	return comms

def sortArr(cell, comms):
	for cm in comms:
		moves = int(cm[0])
		fr = int(cm[1])-1
		to = int(cm[2])-1
		for i in range(moves):
			tHold = cell[fr][0]
			cell[fr].pop(0)
			cell[to].insert(0, tHold)
	return(cell)

def sortArr9001(cell, comms):
	for cm in comms:
		moves = int(cm[0])
		fr = int(cm[1])-1
		to = int(cm[2])-1
		tempHold = cell[fr][:moves]
		cell[fr] = cell[fr][moves:]
		for i in range(len(tempHold)):
			cell[to].insert(i, tempHold[i])
	return cell

cell = parseStacks(lines)
comms = parseCommand(lines)

# sStacks = sortArr(cell, comms)

sStacked = sortArr9001(cell, comms)

final = ""
for s in sStacked:
	final += s[0]

print(final)
