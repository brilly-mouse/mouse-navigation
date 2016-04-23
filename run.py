from mouse import Mouse
from board import Board
import sys

x = 0
y = 0
direction = 0

# can run using python 1 2 3 where it starts at (x,y), direction is left
if(len(sys.argv) >= 4 ):
    x = int(sys.argv[-3])
    y = int(sys.argv[-2])
    direction = int(sys.argv[-1])


board = Board()
mouse = Mouse(x,y,direction,board)


# for i in range(0, 15, 3):
    # for j in range(16):
        # board.addBound(i,j,1)    


print mouse.printBoard()
commands = ('w','a','s','d','q')
while(True):
    command = raw_input("wasd to move, q to quit:")
    if command == 'q':
        break
    else:
        if command == 'w':
            mouse.move()
        elif command == 'a':
            mouse.turnLeft()
        elif command == 's':
            mouse.moveBack()
        elif command == 'd':
            mouse.turnRight()
        
    print mouse.printBoard()
    if( mouse.inGoal()):
        print "You win!!"

