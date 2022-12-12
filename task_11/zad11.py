import math

monke_class = []
divisor = 1
class monke:
	items = []
	inspected = 0
	global monke_class
	def __init__(self, name, s_items, operation, test, if_t_or_f):
		self.name = name
		self.items = s_items
		self.operation = operation
		self.test = test
		self.if_true = int(if_t_or_f[0])
		self.if_false = int(if_t_or_f[1])

	def inspect(self):
		t_len = len(self.items)
		for i in self.items:
			# part 1
			# new_worry = math.floor((self.worry(i))/3)
			# part 2
			new_worry = math.floor(self.worry(i%divisor))
			self.throw(new_worry)
			self.inspected += 1
		self.items = self.items[t_len:]

	def throw(self, item_val):
		if(item_val % self.test == 0):
			monke_class[self.if_true].receive_item(item_val)
		else:
			monke_class[self.if_false].receive_item(item_val)

	def worry(self, item):
		new = 0
		if(self.operation[1] == "old"):
			second_arg = item
		else:
			second_arg = int(self.operation[1])
		if(self.operation[0] == "*"):
			new = item * second_arg
		elif(self.operation[0] == "+"):
			new = item + second_arg
		return new

	def receive_item(self, new_item):
		self.items.append(new_item)

	def ret_inspected(self):
		return self.inspected


lines = []
# with open('zad11_demo.txt') as f:
with open('zad11_input.txt') as f:
	lines = [line.strip() for line in f]

monkees = []
t_or_f = []
def parse_task():
	global t_or_f
	parser = {}
	last = lines[-1]
	for l in lines:
		if(l.startswith("Monkey")):
			parser["name"] = l.rstrip(":")
		if(l.startswith("Starting")):
			t_num_str = list(map(int, l.split(": ")[1].split(", ")))
			parser["items"] = t_num_str
		if(l.startswith("Operation")):
			t_op_str = l.split("= old ")[1].split(" ")
			parser["oper"] = t_op_str
		if(l.startswith("Test")):
			t_test_str = int(l.split("by ")[1])
			parser["test"] = t_test_str
		if(l.startswith("If")):
			if(l.startswith("If true:")):
				t_or_f.append(int(l.split("monkey ")[1]))
			if(l.startswith("If false:")):
				t_or_f.append(int(l.split("monkey ")[1]))
				parser["t_or_f"] = t_or_f
		if(l == '' or l is last):
			monkees.append(parser)
			parser = {}
			t_or_f= []

parse_task()
for m in monkees:
	print(m["test"])
	# part 2 - (learnt a lot about number theory lel) 
	# n*x is divisible by a prime number if (n%23)*x is divisible by 23
	# I can just combine all divisors into super-divisor and reduce everything by that number
	# but still keep the same logic
	divisor *= m["test"]
	monke_class.append(monke(m["name"], m["items"], m["oper"], m["test"], m["t_or_f"]))
print("divisor: ", divisor)
# part 1
# for i in range(20):
# part 2
for i in range(10000):
	for m in monke_class:
		m.inspect()

scores = []
for m in monke_class:
	scores.append(m.ret_inspected())

print(sorted(scores, reverse=True)[1] * sorted(scores, reverse=True)[0])
