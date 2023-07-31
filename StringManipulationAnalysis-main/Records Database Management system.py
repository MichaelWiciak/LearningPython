def showMenu():
	print("1. Show all records")
	print("2. Search by name")
	print("3. Search by department")
	print("4. Pay rise")
	print("5. Transfer")
	print("6. Abandon ship")


def getChoice():
	while True:
		try:
			c = int(input("--->"))
			if c>=1 and c<=6:
				return c
		except ValueError as e:
			raise e


def showRecord(r):
	print("--------------------")
	print("Name:\t\t"+r[0])
	print("Department:\t"+r[1])
	print("Age:\t\t"+str(r[2]))
	print("Salary:\t\t"+"£"+str(r[3]))


def showAllRecords(alist):
	for r in alist:
		showRecord(r)

def searchByName(alist):
	n = input("Enter name: ")
	r = searchIt(alist, 0, n)
	if r != None:
		showRecord(r)
	else:
		print("No such record!")


def searchByDepartment(alist):
	d = input("Enter department: ")
	deplist = getSubList(alist, 1, d)
	if len(deplist)>0:
		showAllRecords(deplist)
	else:
		print("No such department")


def payRiseByDepartment(alist):
	d = input("Enter department: ")
	p = int(input("Pay rise: "))
	deplist = getSubList(alist, 1, d)
	for r in deplist:
		r[3] += p


def transferDepartment(alist):
	n = input("Enter name: ")
	r = searchIt(alist, 0, n)
	if r!= None:
		showRecord(r)
		d = input("Enter department: ")
		r[1] = d
	else:
		print("Huh?")


def searchIt(alist, f, n):
	for r in alist:
		if n == r[f]:
			return r
	return None


def getSubList(alist, f, n):
	newlist = []
	for r in alist:
		if n == r[f]:
			newlist.append(r)
	return newlist


def addEmployee(alist):
	n = input("Name: ")
	d = input("Department: ")
	a = int(input("Age: "))
	s = int(input("Salary: "))
	alist.append([n,d,a,s])


def removeAll(alist):
	check = input("Are you sure (Y/N) ? ")
	if check.upper() in ["Y","YES"]:
		alist = []
	return alist

####### MAIN PROGRAM #########
employeelist = [ ["Alice", "Director", 43,80000], ["Bob", "Finance", 58,50000], ["Cat", "Marketing", 34,32000], ["Des", "IT", 23,45000],["Dan","IT",30,65000],["Nic","IT",30,65000],["Tim","IT",30,100000],["Jeff","Marketing",30,45000],["George","Finance",30,55000] ]
parttime = []


while True:
	print("\n"+str(len(employeelist)), "records\n-----------")
	showMenu()
	try:
		user = getChoice()
		if user == 1:
			showAllRecords(employeelist)
			
		elif user == 2:
			searchByName(employeelist)
			
		elif user == 3:
			searchByDepartment(employeelist)

		elif user == 4:
			payRiseByDepartment(employeelist)

		elif user == 5:
			transferDepartment(employeelist)

		elif user == 6:
			employeelist = removeAll(employeelist)
	except ValueError as e:
		print(e)
		print(type(e))
		print("Numbers Only!\n\n")
