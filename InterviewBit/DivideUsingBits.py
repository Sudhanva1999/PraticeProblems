def divide(A, B): 
		isNeg = 1
		if(A < 0 or B < 0) and not (A < 0 and B < 0):
			isNeg = -1 
		A = abs(A)
		B = abs(B)
		i = 7 
		temp = 0 
		q = 0
		while(i >= 0):
			if((B << i) + temp <= A):
				temp = (B << i) + temp 
				q += 1 << i 
			i -= 1 
			
		return q * isNeg
a,b = map(int,(input("Enter Dividend and Divisor to find their divison without using Divide operator\n").split()))
print(divide(a,b))