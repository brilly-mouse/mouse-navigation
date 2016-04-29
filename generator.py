from mouse import Mouse
from board import Board

b = Board()
mouse = Mouse(0,0,3,b,0)
altfaceWallFunc = lambda self: False
mouse.facingWall = altfaceWallFunc.__get__(mouse, Mouse) # replace facingWall func so mouse can go through walls

print mouse.printBoard()
commands = ('w','a','s','d','b', 'r', 'q','p', 'e',)
while(True):
    command = raw_input("b for bottom wall, r for right wall, e for export:")
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
        elif command == 'p':
            print mouse.AStarSearch()
        elif command == 'b':
            mouse.board.addBound(mouse.x, mouse.y, 2)
        elif command == 'r':
            mouse.board.addBound(mouse.x, mouse.y, 1)
        elif command == 'e':
            mouse.board.save()
        elif command == "read":
            mouse.board.read()
       
        elif len(command.split()) > 0:
            command = command.split()
            if(command[0] == "read"):
                mouse.board.read(command[1])
        
    print mouse.printBoard()

