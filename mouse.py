from Queue import PriorityQueue
class Mouse():
    def __init__(self, xi, yi, direction, board):
        self.x = xi
        self.y = yi
        self.direction = direction
        self.board = board;

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

    def inGoal(self):
        middleCoord = (self.board.sideLength//2 -1, self.board.sideLength//2)
        return self.x in middleCoord and self.y in middleCoord
    
    def manhattanDistance(self):
        lowMiddle = self.board.sideLength//2 -1
        highMiddle = self.board.sideLength//2

        xD = min(abs(lowMiddle - self.x), abs(highMiddle - self.x))
        yD = min(abs(lowMiddle - self.y), abs(highMiddle - self.y))
        return xD + yD

    def euclideanDistance(self):
        lowMiddle = self.board.sideLength//2 -1
        highMiddle = self.board.sideLength//2
        xD = min(abs(lowMiddle - self.x), abs(highMiddle - self.x))
        yD = min(abs(lowMiddle - self.y), abs(highMiddle - self.y))
        return sqrt(xD**2 + yD**2)

    # def AStarSearch():



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






