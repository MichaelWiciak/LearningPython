import time

LIST = []

while True:
	try:
		a = time.clock()
		a_file = open("FILENAME.py", "r") ### Any file Name
		exec(a_file.read())
		b = time.clock()
		Time = b - a
		LIST.append(Time)
	except KeyboardInterrupt:
		break

LIST = str(LIST).strip('[]')
execel_file = open("Results.csv", "w")
execel_file.write(LIST)
	





	
	

	
