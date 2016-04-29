from board import Board
class SimRun():
    def __init__(self, mouse, board):
        self.mouse = mouse
        self.omniscientBoard = board
        
    def move(self):
        coordTuple = self.mouse.forwardCoordinates()
        if not self.mouse.facingWall() and self.mouse.inBounds(coordTuple[0], coordTuple[1]):
           (self.mouse.x, self.mouse.y) = self.mouse.forwardCoordinates()
        if self.mouse.facingWall():
            print "Mouse is facing wall"

        # move a certain distance and try to make sure that
        # mouse stays in the center
        # decrease or increase speed appropriately for next move
    def moveBack(self):
        self.mouse.turnRight()
        self.mouse.turnRight()
        self.mouse.move()
        self.mouse.turnRight()
        self.mouse.turnRight()

    def facingWall(self):
        return self.omniscientBoard.boundaries[self.mouse.x][self.mouse.y][self.mouse.direction]
        #move backwards, similar to move() but reversed
    def turnRight(self):
        self.mouse.direction = (self.mouse.direction + 1)%4
    def turnLeft(self):
        self.mouse.direction = (self.mouse.direction - 1 + 4)%4

    def printBoard(self):
        line = "||"

        for x in range(self.mouse.board.sideLength):
            if self.omniscientBoard.boundaries[x][0][1]:
                if self.mouse.board.boundaries[x][0][1]:
                    line += "===|"
                else:
                    line += "===%"
            else:
                line += "===="
        line = line + "|\n"
        for y in range(self.mouse.board.sideLength):
            for row in range(2):
                line += "||"
                for x in range(self.mouse.board.sideLength):
                    initial = ["   ", " "]
                    # should only print according to what is on bottom and right, since adding left
                    # and top is redundant with multiple boxes printed together.
                    box = self.mouse.board.boundaries[x][y]
                    omniscientBox = self.omniscientBoard.boundaries[x][y]
                    if omniscientBox[1]:
                        if box[1]:
                            initial[1] = "|"
                        else:
                            initial[1] = "%"
                    if x in (7,8) and y in (7,8):
                        initial[0] = "GGG"
                        if(x == self.mouse.x and y == self.mouse.y):
                            initial[0] = "G{0}G".format(self.mouse.printDirection())
                        if x == 7:
                            initial[1] = "G" #override possiblity of vertical wall inside goal area
                    elif row == 0: 
                        if(x == self.mouse.x and y == self.mouse.y):
                            initial[0] = " {0} ".format(self.mouse.printDirection())
                        elif (x,y) in self.mouse.saved_path:
                            initial[0] = " * "
                    elif row == 1:
                        if omniscientBox[2]:
                            if box[2]:
                                if(y == self.mouse.board.sideLength -1):
                                    initial[0] = "==="
                                    initial[1] = "="
                                else:
                                    initial[0]= "---"
                                    initial[1] = "-"
                            else:
                                if(y == self.mouse.board.sideLength -1):
                                    initial[0] = "%%%"
                                    initial[1] = "%"
                                else:
                                    initial[0]= "%%%"
                                    initial[1] = "%"

                        if omniscientBox[1]:
                            if(box[1]):
                                initial[1] = "|"
                            else:
                                initial[1] = "%"

                    line += "".join(initial)
                line +="|\n"
        return line
 
