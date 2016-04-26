from Queue import PriorityQueue
class Mouse():
    def __init__(self, xi, yi, direction, board):
        self.x = xi
        self.startX = xi
        self.startY = yi
        self.y = yi
        self.direction = direction
        self.board = board;
        self.saved_path = []

    """
    Changes x and y if moving forward is open and in bounds
    """
    def move(self):
        if not self.facingWall() and self.inBounds(self.forwardCoordinates()):
           (self.x, self.y) = self.forwardCoordinates()
        if self.facingWall():
            print "Mouse is facing wall"

    """
    Returns coordinates of moving forward one move in (x,y) form

    """
    def forwardCoordinates(self):
        if self.direction==0:
            return (self.x, self.y-1)
        elif self.direction ==1:
            return (self.x + 1, self.y)
        elif self.direction ==2:
            return (self.x, self.y + 1)
        else:
            return (self.x -1, self.y)

    def moveBack(self):
        self.turnRight()
        self.turnRight()
        self.move()
        self.turnRight()
        self.turnRight()

    def facingWall(self):
        return self.board.boundaries[self.x][self.y][self.direction]

    def turnRight(self):
        self.direction = (self.direction + 1)%4

    def turnLeft(self):
        self.direction = (self.direction - 1 + 4)%4
    def inBounds(self, xy):
        x = xy[0]
        y = xy[1]
        return x >= 0 and x < self.board.sideLength and y >= 0 and y < self.board.sideLength
    def inBounds(self, x,y):
        return x >= 0 and x < self.board.sideLength and y >= 0 and y < self.board.sideLength

    def inGoal(self, x= None, y=None):
        if(x == None and y == None):
            x = self.x
            y = self.y
        middleCoord = (self.board.sideLength//2 -1, self.board.sideLength//2)
        return x in middleCoord and y in middleCoord
    
    def manhattanDistance(self, x= None, y=None):
        if(x == None and y == None):
            x = self.x
            y = self.y
        lowMiddle = self.board.sideLength//2 -1
        highMiddle = self.board.sideLength//2

        xD = min(abs(lowMiddle - x), abs(highMiddle - x))
        yD = min(abs(lowMiddle - y), abs(highMiddle - y))
        return xD + yD

    def euclideanDistance(self, x= None, y=None):
        if(x == None and y == None):
            x = self.x
            y = self.y
        lowMiddle = self.board.sideLength//2 -1
        highMiddle = self.board.sideLength//2
        xD = min(abs(lowMiddle - x), abs(highMiddle - x))
        yD = min(abs(lowMiddle - y), abs(highMiddle - y))
        return sqrt(xD**2 + yD**2)


    """
    Returns a list of (x,y) coordinates to take to reach the goal
    """
    def AStarSearch(self):
        nodesToSearch = PriorityQueue()
        first=  Node(self.x,self.y, self)
        nodesToSearch.put(first)
        visited = [[0 for _x in range(self.board.sideLength)] for _y in range(self.board.sideLength)]
        visited[first.x][first.y] = 1
        directions = [0,1,2,3]

        solution = first # temp value, will be replaced when reached the end
        while not nodesToSearch.empty():
            parent = nodesToSearch.get() # first node pulled out
            print "parent " + str(parent.x) + " " + str(parent.y) + " priority " + str(parent.priority)

            visited[parent.x][parent.y] = 1
            if self.board.inGoal(parent.x, parent.y): # reached goal
                print "solution reached"
                s = str(parent.x) + " " + str(parent.y)
                print s
                solution = parent
                break
            neighbors = zip(directions,self.board.neighbors(parent.x, parent.y))
            # print neighbors
            for d,coord, in neighbors:
                n = (Node(coord[0],coord[1],self,parent.distance, parent))
                if self.board.inBounds(coord[0],coord[1]) and self.board.boundaries[parent.x][parent.y][d] == 0 and visited[coord[0]][coord[1]] == 0:
                    n = (Node(coord[0],coord[1],self,parent.distance, parent))
                    nodesToSearch.put(n)
            # toVisit = [Node(coord[0],coord[1],self,parent.distance, parent) for d,coord in neighbors if self.board.inBounds(coord[0],coord[1]) and self.board.boundaries[coord[0]][coord[1]][d] == 0 and visited[coord[0]][coord[1]] == 0]
            # toVisit is the neighbor spaces that are unvisited, have no boundaries, in bounds
            # for n in toVisit:
                # nodesToSearch.put(n)
                    print "possible " + str(n.x) + " " + str(n.y) + " " + str(n.priority) + " " + str(d) 
                    print str(self.board.inBounds(coord[0],coord[1])) +  str(self.board.boundaries[parent.x][parent.y][d]) +  str(visited[coord[0]][coord[1]] == 0)

        path = []

        while solution is not  None:
            path = [(solution.x, solution.y)] + path
            solution = solution.parent
        self.saved_path  = path
        return path





    def printDirection(self):
        if self.direction == 0:
            return "^"
        elif self.direction == 1:
            return ">"
        elif self.direction ==2:
            return "V"
        else:
            return "<"


    def printBoard(self):
        line = "||"

        for x in range(self.board.sideLength):
            if self.board.boundaries[x][0][1]:
                line += "===|"
            else:
                line += "===="
        line = line + "|\n"
        for y in range(self.board.sideLength):
            for row in range(2):
                line += "||"
                for x in range(self.board.sideLength):
                    initial = ["   ", " "]
                    # should only print according to what is on bottom and right, since adding left
                    # and top is redundant with multiple boxes printed together.
                    box = self.board.boundaries[x][y]
                    if box[1]:
                        initial[1] = "|"

                    if x in (7,8) and y in (7,8):
                        initial[0] = "GGG"
                        if(x == self.x and y == self.y):
                            initial[0] = "G{0}G".format(self.printDirection())
                        if x == 7:
                            initial[1] = "G" #override possiblity of vertical wall inside goal area
                    elif row == 0: 
                        if(x == self.x and y == self.y):
                            initial[0] = " {0} ".format(self.printDirection())
                        elif (x,y) in self.saved_path:
                            initial[0] = " * "
                        # if box[1]:
                            # initial[1] = "|"
                    elif row == 1:

                        if( box[2]):
                            if(y == self.board.sideLength -1):
                                initial[0] = "==="
                                initial[1] = "="
                            else:
                                initial[0]= "---"
                                initial[1] = "-"
                        if(box[1]):
                            initial[1] = "|"
                    line += "".join(initial)
                line +="|\n"
        return line





class Node():
    def __init__(self, x,y, mouse, distance=-1, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.mouse = mouse
        self.distance = distance + 1
        self.priority = mouse.manhattanDistance(x,y) + self.distance

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

