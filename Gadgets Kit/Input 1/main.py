def find_hcf(args=list()) -> int:
	def find_gcd(x, y): 
	    while(y): 
	        x, y = y, x % y 
	  
	    return x 
	  
	num1=args[0] 
	num2=args[1] 
	gcd=find_gcd(num1,num2) 
	  
	for i in range(2,len(args)): 
	    gcd=find_gcd(gcd,args[i]) 
	      
	return gcd


with open('input.txt', 'r') as file:
	lines = [line.strip('\n') for line in file.readlines()]
	# print(lines)
	
curr_line = 0 # meaning the current line in the lines list
T = int(lines[curr_line]) # Meaning number of test cases
curr_line += 1

outputs = list()

for test_case in range(1, T+1):
	N = int(lines[curr_line]) # meaning number of distinct gadgets
	curr_line += 1 

	# this line gets a list with each item as the number of items for each
	# gadget eg, if I have 2 shirts and 5 stickers then the list will
	# look like this no_gadgets = [2, 5]
	no_gadgets = [int(gadget) for gadget in lines[curr_line].split(' ')]
	curr_line += 1

	if len(no_gadgets)!=N:
		break

	hcf = find_hcf(no_gadgets) # meaning all diff possible combos with equally divided gadgets

	combo = 0
	for i in range(1, hcf+1):
		if hcf%i==0:
			combo += 1

	outputs.append(f"Case #{test_case}: {combo}")

with open('output.txt', 'w+') as out_file:
	for output in outputs:
		out_file.write(f"{output}\n")