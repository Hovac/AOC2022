with open('zad2.txt') as f:
	lines = [line.rstrip() for line in f]

rock = 1 #  X   A
paper = 2 # Y   B
scissors = 3 #  Z   C

A = X = "rock"
B = Y = "paper"
C = Z = "scissors"

lose = 0
draw = 3
win = 6

def winner(f1, f2):
	if(((f1 == "A") & (f2 == "X")) | ((f1 == "B") &  (f2 == "Y")) | ((f1 == "C") & (f2 == "Z"))):
		if(f2 == "X"):
			pulled = 1
		elif(f2 == "Y"):
			pulled = 2
		else:
			pulled = 3
		return (draw + pulled)
	elif(f1 == "A"):
		if(f2 == "Y"):
			print("rock falls to paper - you win score: ",(win+paper))
			return (win + paper)
		else:
			print("rock beats scissors - you lose score: ",(lose + scissors))
			return (lose + scissors)
	elif(f1 == "B"):
		if(f2 == "X"):
			print("paper beats rock - you lose score: ",(lose + rock))
			return (lose + rock)
		else:
			print("paper is beaten by scissors - you win score: ",(win + scissors))
			return (win + scissors)
	elif(f1 == "C"):
		if(f2 == "X"):
			print("scissors are beaten by rock - you win score: ",(win + rock))
			return (win + rock)
		else:
			print("scissors beat paper - you lose score: ",(lose + paper))
			return (lose + paper)

# X -> lose
# Y -> draw
# Z -> win

A = X = "rock"
B = Y = "paper"
C = Z = "scissors"

def second(f1, f2):
	pulled = 0
	if(f2 == "X"):
		if(f1 == "A"):
			pulled = scissors
		elif(f1 == "B"):
			pulled = rock
		elif(f1 == "C"):
			pulled = paper
		print("lose ", pulled, lose)
		return (lose + pulled)
	if(f2 == "Y"):
		if(f1 == "A"):
			pulled = rock
		elif(f1 == "B"):
			pulled = paper
		elif(f1 == "C"):
			pulled = scissors
		print("draw ", pulled, draw)
		return (draw + pulled)
	if(f2 == "Z"):
		if(f1 == "A"):
			pulled = paper
		elif(f1 == "B"):
			pulled = scissors
		elif(f1 == "C"):
			pulled = rock
		print("win ", pulled, win)
		return (win + pulled)


sum = 0

for i in lines:
	sum += second(i[0], i[2])

print(sum)

# print(lines)