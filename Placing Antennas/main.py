with open('input.txt', 'r') as file:
	lines = [line.strip('\n') for line in file.readlines()]
	# print(lines)
	
curr_line = 0 # meaning the current line in the lines list
T = int(lines[curr_line]) # Meaning number of test cases
curr_line += 1

outputs = list()

for test_case in range(1, T+1):
	# here n is number of buildings/antennas 
	# and k is number of antennas to be used to find
	# the minimum and maximum score
	n, k = [int(i) for i in lines[curr_line].split()]
	curr_line += 1 

	# b_scores meaning the scores for each building
	b_scores = [int(b) for b in lines[curr_line].split()]
	curr_line += 1

	# a_scores means the scores for each antenna
	a_scores = [int(a) for a in lines[curr_line].split()]
	curr_line += 1

	if len(a_scores)!=n or len(b_scores)!=n:
		break


	# ----- FOR MAXIMUM ------
	maximum_score = 0

	copy_a = a_scores
	copy_b = b_scores

	for antenna in range(k):

		high_a = max(copy_a)
		high_b = max(copy_b)

		copy_a.remove(high_a)
		copy_b.remove(high_b)

		maximum_score += high_b*high_a

	# ----- FOR MINIMUM -----
	minimum_score = 0

	copy_a = a_scores
	copy_b = b_scores

	for antenna in range(k):

		low_a = min(copy_a)
		low_b = min(copy_b)

		copy_a.remove(low_a)
		copy_b.remove(low_b)

		minimum_score += low_b*low_a


	outputs.append(f"Case #{test_case}: {minimum_score} {maximum_score}")

with open('output.txt', 'w+') as out_file:
	for output in outputs:
		out_file.write(f"{output}\n")