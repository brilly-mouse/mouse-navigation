class SimRun():
    def __init__(self, mouse):
        self.mouse = mouse
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
        return self.mouse.board.boundaries[self.mouse.x][self.mouse.y][self.mouse.direction]
        #move backwards, similar to move() but reversed
    def turnRight(self):
        self.mouse.direction = (self.mouse.direction + 1)%4
    def turnLeft(self):
        self.mouse.direction = (self.mouse.direction - 1 + 4)%4
