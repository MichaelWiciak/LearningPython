import turtle
turtle.ht()
turtle.tracer(0, 0)

def drawGrid(size):
    turtle.pu()
    turtle.goto(-400, -400)
    turtle.pd()
    turtle.setheading(0)
    for x in range(size+1):
        turtle.pu()
        turtle.setx(-400)
        turtle.sety(-400+(800/size)*x)
        turtle.pd()
        turtle.fd(800)
    turtle.setheading(90)
    for y in range(size+1):
        turtle.pu()
        turtle.sety(-400)
        turtle.setx(-400+(800/size)*y)
        turtle.pd()
        turtle.fd(800)
    turtle.update()

class Stack(object):
    def __init__(self, size):
        self.__size = size
        self.__stack = []
        for x in range(self.__size):
            self.__stack.append(None)
        self.__TOS = -1

    def empty(self):
        return self.__TOS == -1

    def full(self):
        return self.__TOS == self.__size-1

    def pop(self):
        self.__TOS -= 1
        if self.empty():
            raise StackException("Stack empty error.")
        return self.__stack[self.__TOS]
    
    def push(self, value):
        self.__TOS += 1
        self.__stack[self.__TOS] = value

    def get(self):
        return self.__stack

    def getTOS(self):
        return self.__stack[self.__TOS]


class StackException(Exception):
    def __init__(self, value):
        self.value = value
        
        
class DFS(object):
    def __init__(self, size):
        self.__size = size
        self.__nodes = {}
        self.__coords = {}
        self.__visited = {}
        self.__route = Stack(self.__size**2)
        self.__checked = {}
        for x in range(self.__size):
            self.__coords[x] = {}
            for y in range(self.__size):
                n = (x * self.__size + y)
                self.__checked[n] = []
                self.__coords[x][y] = n
                self.__nodes[n] = []
                self.__visited[n] = False
        for x in range(self.__size):
            for y in range(self.__size):
                node = self.__coords[x][y]
                for i in [-2, -1, 1, 2]:
                    for j in [-2, -1, 1, 2]:
                        if i**2 != j**2 and 0 <= x+i < self.__size and 0 <= y+j < self.__size:
                            self.__nodes[node].append(self.__coords[x+i][y+j])

    def findLonely(self, nodes, current):
        highscore = 9
        node = None
        for n in nodes:
            if n not in self.__checked[current] and not self.__visited[n]:
                score = 0
                for x in self.__nodes[n]:
                    if not self.__visited[x]:
                        score += 1
                if score < highscore:
                    highscore = score
                    node = n
        if node is not None:
            self.__checked[current].append(node)
        return node

    def main(self, node):
        done = False
        pos = 0
        turtle.tracer(1, 10)
        turtle.pencolor("Red")
        turtle.pu()
        turtle.goto(((node%self.__size)*800/self.__size - 400 + 400/self.__size), (int(node/self.__size)*800/self.__size - 400 + 400/self.__size))
        turtle.pd()
        turtle.write(pos)
        while not done:
            self.__visited[node] = True
            self.__route.push(node)
            found = False
            while not found:
                if self.__route.full():
                    return self.__route.get()
                n = self.findLonely(self.__nodes[node], node)
                if n is None:
                    self.__visited[node] = False
                    self.__checked[node] = []
                    try:
                        node = self.__route.pop()
                    except StackException:
                        return "No Route"
                    pos -= 1
                    turtle.undo()
                else:
                    node = n
                    found = True
                    pos += 1
                    turtle.goto(((node%self.__size)*800/self.__size - 400 + 400/self.__size), (int(node/self.__size)*800/self.__size - 400 + 400/self.__size))
if __name__ == "__main__":                    
    size = int(input("Input Size:\n>>> "))
    drawGrid(size)
    app = DFS(int(size))
    route = app.main(0)
    if route != "No Route":
        turtle.pencolor("Red")
        turtle.pu()
        for n in route:
            turtle.goto(((n%size)*800/size - 400 + 400/size), (int(n/size)*800/size - 400 + 400/size))
            turtle.write(route.index(n))
    input(route)
		
