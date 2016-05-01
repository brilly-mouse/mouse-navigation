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

    




