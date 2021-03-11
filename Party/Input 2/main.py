with open('input.txt', 'r') as file:
	lines = [line.strip('\n') for line in file.readlines()]
	# print(lines)
	
curr_line = 0 # meaning the current line in the lines list
T = int(lines[curr_line])
curr_line += 1
outputs = list()
for test_case in range(1, T+1):
	N = int(lines[curr_line])
	curr_line += 1
	degrees = [int(degree) for degree in lines[curr_line].split(' ')]
	curr_line += 1

	if len(degrees)!=N:
		break

	beauty = 0

	for degree in degrees:
		if degree>=0:
			beauty += degree

	# print(test_case, beauty)
	outputs.append(f"Case #{test_case}: {beauty}")
	# print(f"Case #{test_case}: {beauty}")
	# print("N ", N)
	# print("degrees" ,degrees)

with open('output.txt', 'w+') as out_file:
	for output in outputs:
		out_file.write(f"{output}\n")