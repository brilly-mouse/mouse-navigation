class LiveRun():
    def __init__(self, mouse):
        self.mouse = mouse
    def move(self):
        # move a certain distance and try to make sure that
        # mouse stays in the center
        # decrease or increase speed appropriately for next move
        # MAKE SURE TO UPDATE self.mouse.x and self.mouse.y when moving appropriately
        return -1
    
    def moveBack(self):
        #move backwards, similar to move() but reversed
        # MAKE SURE TO UPDATE self.mouse.x and self.mouse.y when moving appropriately
        return -1

    def turnRight(self):
        # decrease speed appropriately for turn
        # MAKE SURE TO UPDATE self.mouse.direction
        # turn right
        return -1

    def turnLeft(self):
        # decrease speed appropriately for turn
        # MAKE SURE TO UPDATE self.mouse.direction
        # turn left
        return -1

    def facingWall(self):
        # returns whether wall is directly in front of mouse
        return -1


    ################### BELOW ARE METHODS EXCLUSIVE TO LIVE MOUSE ########################
    """
    This method is called when mouse position in square is far enough to detect next wall ahead
    """
    def detectFrontRightWall(self):
        hasWall = -1 # 1 or 0, set detection to check
        forwardCoord = self.mouse.forwardCoordinates()
        if(hasWall != self.mouse.boundaries[forwardCoord[0]][forwardCoord[1]][self.mouse.direction]):
            # somehow update self.mouse.boundaries to reflect appropriate changes

            return -1
        else:
            return 1 # wall found as expected

            
        return -1;
    
    
    def detectFrontLeftWall(self):
        return -1

    def detectFrontWall(self):
        return -1

    def detectFrontWallDistance(self):
        return -1


########################## BELOW METHODS MAY BELONG IN MOUSE.PY ######################

    """ Floodfill algorithm """
    def floodFillToGoal(self):
        while(not self.mouse.inGoal):
            self.mouse.path = self.mouse.AStarSearch
            self.followPath()
            # will follow path to completion if walls appropriate
            # recalculates path if followpath returns

    """
    Keeps moving mouse to through path. Returns if path completed or walls are updated
    """
    def followPath(self, path):
        while(self.mouse.path):
            moveSuccess = self.moveToSquare(self.mouse.x, self.mouse.y)
            if moveSuccess:
                self.mouse.path = self.mouse.path[1:] # truncate after sucessful move
            else:
                return # when found walls unexpected
        return # when finished following the path
    
    """
    Turns and moves to a new position, which should be adjacent to current spot. If new wall changes updated, returns 0
    """
    def moveToSquare(self,x,y):
        #1) turn to correct direction
        #2) move forward or backward
        # when in range to see front right wall, call detectFrontRightWall or detectFrontLeftWall
        # return 1 if moved to square as expected
        # return 0 if boundaries found to be different

        return -1


