from random import shuffle

with open('input.txt', 'r') as file:
	lines = [line.strip('\n') for line in file.readlines()]
	# print(lines)
	
curr_line = 0 # meaning the current line in the lines list
T = int(lines[curr_line]) # Meaning number of test cases
curr_line += 1

outputs = list()

for test_case in range(1, T+1):
	# here n is number of number of seats
	# and k is number of days
	n, k = [int(i) for i in lines[curr_line].split()]
	curr_line += 1 

	seating = [seat for seat in lines[curr_line].split()]
	curr_line += 1

	shuffle(seating)

	randommed = ' '.join(seating)


	outputs.append(f"Case #{test_case}: {randommed}")

with open('output.txt', 'w+') as out_file:
	for output in outputs:
		out_file.write(f"{output}\n")