def decode(t):
	s = ""
	for i in range(0,len(t),2):
		num = int(t[i])
		s = s + t[i+1]*num
	return s


def encode(astring):
	compressed = ""
	i = 1             
	count = 1         
	current = astring[0] 
	while i<len(astring):
		if current != astring[i] or count>8:
			compressed = compressed + str(count) + current
			count = 1
			current = astring[i] 
		elif current == astring[i]:
			count = count + 1
		i += 1
	compressed = compressed + str(count) + current
	return compressed
