lines = []
with open('zad7.txt') as f:
	lines = [line.rstrip("\n") for line in f]

dirs = []

# def create_tree():
# 	cur_dir = []
# 	sum = 0
# 	for l in lines:
# 		if(("ls" in l) or ("dir" in l)):
# 			continue
# 		else:
# 			if("cd" in l):
# 				if(not ".." in l):
# 					dirs.append(l[5:])
# 					cur_dir.append(dirs[-1])
# 					sum = 0
# 				elif("cd /" in l):
# 					cur_dir = []
# 				else:
# 					cur_dir.pop()
# 			else:
# 				dir_struct = {
# 					"full_path": "",
# 					"size": ""
# 				}
# 				sum += int(l.split(" ")[0])
# 				dir_struct["full_path"] = "/".join(cur_dir)
# 				# edge case if there is only root present
# 				if(len(dir_struct["full_path"]) > 1):
# 					dir_struct["full_path"] = dir_struct["full_path"][1:]
# 				print(dir_struct["full_path"])
# 				dir_struct["size"] = sum
# 				dir_sizes.append(dir_struct)

files_path = []
file = {}

def create_tree():
	cur_dir = []
	sum = 0
	for l in lines:
		if(("$ ls" in l) or ("dir" in l)):
			continue
		else:
			if("cd" in l):
				if(not ".." in l):
					dirs.append(l[5:])
					cur_dir.append(dirs[-1])
				elif("cd /" in l):
					cur_dir = []
				else:
					cur_dir.pop()
			elif(l[0].isdigit()):
				sum += int(l.split(" ")[0])
				tStr = ""
				if(not cur_dir[-1] == "/"):
					tStr = "/" + "/".join(cur_dir[1:]) + "/" + l.split(" ")[1]
				else:
					tStr ="/" + l.split(" ")[1]
				file[tStr] = l.split(" ")[0]


create_tree()

print(file)
