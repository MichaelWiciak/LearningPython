def rightShift(n, bits):
	leftside = "0" * n 
	rightside = ""
	for i in range(len(bits) - n):
		rightside = rightside + bits[i]
	return leftside + rightside