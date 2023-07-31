import re

pattern = "^a.c"
target = "ay8cdefgh"

if re.match(pattern, target):
	print("Matched")
else:
	print("No match")
