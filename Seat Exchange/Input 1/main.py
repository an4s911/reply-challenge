	def find_gcd(x, y): 
	    while(y): 
	        x, y = y, x % y 
	  
	    return x 
	      
	      
	l = [40, 88, 32, 40, 48, 32, 40, 24] 
	  
	num1=l[0] 
	num2=l[1] 
	gcd=find_gcd(num1,num2) 
	  
	for i in range(2,len(l)): 
	    gcd=find_gcd(gcd,l[i]) 
	      
	print(gcd)