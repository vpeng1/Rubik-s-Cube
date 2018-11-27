# import everything from rubikMoves
from rubikMoves import *
from RubiksCube import *

colors = {"yellow": set(range(9)), "red": set(range(9, 18)), "green":
            set(range(18, 27)), "orange": set(range(27, 36)), "blue":
            set(range(36, 45)), "white": set(range(45, 54))}

def convertBoardToCube(board):
    edges = [{7,19}, {14,21}, {23,30}, {25,46}, {5,28}, {3,10}, {1,37}, {32,39},
         {34,50}, {43,52}, {41,12}, {16,48}]
    corners = [{6,11,18}, {8,20,27}, {17,24,45}, {26,33,47}, {2,29,36}, {35,42,53},
           {15,44,51}, {0,9,38}]

    c = [[[None, None, None] for i in range(3)] for j in range(6)]
    findCorners(board, c)
    findEdges(board, c)
    findCenters(c)
    return Cube(c)
    # for face in range(len(board)):
    #     for row in range(len(board[0])):
    #         for col in range(len(board[0][0])):
    #             pass

def findCorners(board, c):
    # places all the corners in the board
    cornersToNumbers = {("white", "red", "green"): (45, 17, 24),
                        ("white", "blue", "red"): (51, 44, 15),
                        ("white", "orange", "blue"): (53, 35, 42),
                        ("white", "green", "orange"): (47, 26, 33),
                        ("yellow", "red", "blue"): (0, 9, 38),
                        ("yellow", "green", "red"): (6, 18, 11),
                        ("yellow", "orange", "green"): (8, 27, 20),
                        ("yellow", "blue", "orange"): (2, 36, 29)}
    corners = {(board[0][0][0], board[1][0][0], board[4][0][2]): [(0, 0, 0), (1, 0, 0), (4, 0, 2)],
               (board[0][0][2], board[4][0][0], board[3][0][2]): [(0, 0, 2), (4, 0, 0), (3, 0, 2)],
               (board[0][2][0], board[2][0][0], board[1][0][2]): [(0, 2, 0), (2, 0, 0), (1, 0, 2)],
               (board[0][2][2], board[3][0][0], board[2][0][2]): [(0, 2, 2), (3, 0, 0), (2, 0, 2)],
               (board[5][0][0], board[1][2][2], board[2][2][0]): [(5, 0, 0), (1, 2, 2), (2, 2, 0)],
               (board[5][0][2], board[2][2][2], board[3][2][0]): [(5, 0, 2), (2, 2, 2), (3, 2, 0)],
               (board[5][2][0], board[4][2][2], board[1][2][0]): [(5, 2, 0), (4, 2, 2), (1, 2, 0)],
               (board[5][2][2], board[3][2][2], board[4][2][0]): [(5, 2, 2), (3, 2, 2), (4, 2, 0)]}
    for corner in corners:
        for corn in cornersToNumbers:
            if set(corner) == set(corn):
                for i in range(len(corner)):
                    for j in range(len(corn)):
                        if corner[i] == corn[j]:
                            face, row, col = corners[corner][i]
                            c[face][row][col] = cornersToNumbers[corn][j]


def findEdges(board, c):
    edgesToNumbers = {("yellow", "green"): (7,19), ("red", "green"): (14,21),
                      ("green", "orange"): (23,30), ("green", "white"): (25,46),
                      ("yellow", "orange"): (5,28), ("yellow", "red"): (3,10),
                      ("yellow", "blue"): (1,37), ("orange", "blue"): (32,39),
                      ("orange", "white"): (34,50), ("blue", "white"): (43,52),
                      ("blue", "red"): (41,12), ("red", "white"): (16,48)}
    edges = {(board[0][0][1], board[4][0][1]): [(0, 0, 1), (4, 0, 1)],
             (board[0][1][0], board[1][0][1]): [(0, 1, 0), (1, 0, 1)],
             (board[0][1][2], board[3][0][1]): [(0, 1, 2), (3, 0, 1)],
             (board[0][2][1], board[2][0][1]): [(0, 2, 1), (2, 0, 1)],
             (board[5][0][1], board[2][2][1]): [(5, 0, 1), (2, 2, 1)],
             (board[5][1][0], board[1][2][1]): [(5, 1, 0), (1, 2, 1)],
             (board[5][1][2], board[3][2][1]): [(5, 1, 2), (3, 2, 1)],
             (board[5][2][1], board[4][2][1]): [(5, 2, 1), (4, 2, 1)],
             (board[1][1][0], board[4][1][2]): [(1, 1, 0), (4, 1, 2)],
             (board[1][1][2], board[2][1][0]): [(1, 1, 2), (2, 1, 0)],
             (board[2][1][2], board[3][1][0]): [(2, 1, 2), (3, 1, 0)],
             (board[3][1][2], board[4][1][0]): [(3, 1, 2), (4, 1, 0)]}
    for edge in edges:
        for ed in edgesToNumbers:
            if set(edge) == set(ed):
                for i in range(len(edge)):
                    for j in range(len(ed)):
                        if edge[i] == ed[j]:
                            face, row, col = edges[edge][i]
                            c[face][row][col] = edgesToNumbers[ed][j]


def findCenters(c):
    # centers are always in the same positions no matter the scramble
    c[0][1][1] = 4
    c[1][1][1] = 13
    c[2][1][1] = 22
    c[3][1][1] = 31
    c[4][1][1] = 40
    c[5][1][1] = 49

def randomScramble(scramble):
    return scrambleCube(scramble)

def cubeToBoard(moveCube, colors):
    cube = moveCube.getListCube()
    c = [[[None for i in range(3)] for j in range(3)] for k in range(6)]
    for face in range(len(cube)):
        for row in range(len(cube[0])):
            for col in range(len(cube[0][0])):
                for color in colors:
                    if cube[face][row][col] in colors[color]:
                        c[face][row][col] = color
    return c


# animation template from 112 website
from tkinter import *
def init(data):
    data.colors = ["yellow", "red", "green", "orange", "blue", "white"]
    data.board = [[["grey" for k in range(3)]for j in range(3)] for i in range(6)]
    for face in range(len(data.board)):
        data.board[face][1][1] = data.colors[face]
    data.selectedColor = "white"
    data.colorWidth = data.width/6
    data.colorHeight = data.height/10
    data.stickerSize = data.width/12
    data.cubeHeight = data.height/3 + data.colorHeight
    data.canSolve = True
    data.scramble = None
    data.solution = None
    data.time = 0
    data.i = 0
    data.currMove = None
    data.isSolved = False
    data.solved = [[[color for i in range(3)] for j in range(3)] for color in colors]
    data.pause = False
    data.fastSolve = False
    data.speed = 20
    data.prevMove = False

def mousePressed(event, data):
    if 0 <= event.y <= data.colorHeight:
        for i in range(6):
            if i*data.colorWidth <= event.x < (i+1)*data.colorWidth:
                data.selectedColor = data.colors[i]
    elif data.cubeHeight <= event.y < data.cubeHeight+3*data.stickerSize:
        i = 0
        h = data.cubeHeight
        for face in range(len(data.board)):
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if (col+i-3)*data.stickerSize <= event.x <= (col+i-2)*data.stickerSize:
                        if h+row*data.stickerSize <= event.y <= h+(row+1)*data.stickerSize:
                            data.board[face][row][col] = data.selectedColor
            i += 3
    elif 3*data.stickerSize <= event.x < 6*data.stickerSize:
        # data.cubeHeight - 3*data.stickerSize <= event.y < data.cubeHeight:
        h = data.cubeHeight
        for face in [0, 5]:
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if (col+3)*data.stickerSize <= event.x < (col+4)*data.stickerSize:
                        if face == 0:
                            if h+(row-3)*data.stickerSize <= event.y < h+(row-2)*data.stickerSize:
                                data.board[face][row][col] = data.selectedColor
                        elif h+(row+3)*data.stickerSize <= event.y < h+(row+4)*data.stickerSize:
                                data.board[face][row][col] = data.selectedColor
    elif data.width - 3*data.stickerSize <= event.x < 0.95*data.width and \
                    7*data.height/8 <= event.y < 0.95*data.height:
        print("Solving...")
        for face in data.board:
            for row in face:
                if "grey" in row:
                    data.canSolve = False
        if data.canSolve:
            c = convertBoardToCube(data.board)
            print("c is", c)
            try:
                data.solution = solveCube(c)
                data.scramble = None
            except:
                print("Cube is Unsolvable")
        else:
            print("Cube is Unsolvable")
    elif data.width - 3*data.stickerSize <= event.x < 0.95*data.width and \
            6*data.height/8 <= event.y < 6*data.height/8 + 0.075*data.height:
        data.scramble = scrambleAlgorithm()
        r = randomScramble(data.scramble)
        c = cubeToBoard(r, colors)
        # print(c)
        data.board = c
    else:
        pauseX = data.width - 3*data.stickerSize
        pauseY = data.colorHeight + 3*data.stickerSize
        r = data.width/30
        pauseDist = ((pauseX-event.x)**2 + (pauseY-event.y)**2)**0.5
        if pauseDist < r:
            data.pause = not data.pause
        speedUpX = data.width - 1.5*data.stickerSize
        speedUpY = pauseY
        speedDist = ((speedUpX-event.x)**2 + (speedUpY-event.y)**2)**0.5
        if speedDist < r:
            data.fastSolve = not data.fastSolve
        prevMoveX = data.width - 4.5*data.stickerSize
        prevMoveY = pauseY
        prevDist = ((prevMoveX-event.x)**2 + (prevMoveY-event.y)**2)**0.5
        if prevDist < r:
            data.prevMove = not data.prevMove





def keyPressed(event, data):
    c = Cube(data.board)
    data.board = c.cube
    if data.solution == None:
        # only allows changes if the cube is not solving itself
        if event.keysym == "r":
            c.turnRight()
        elif event.keysym == "l":
            c.turnLeft()
        elif event.keysym == "u":
            c.turnUp()
        elif event.keysym == "d":
            c.turnDown()
        elif event.keysym == "f":
            c.turnFront()
        elif event.keysym == "b":
            c.turnBack()
    if event.keysym == "q":
        init(data)

def timerFired(data):
    c = Cube(data.board)
    if not data.pause:
        data.time += 1
        if data.solution != None:
            data.board = c.cube
            if data.time % data.speed == 0:
                try:
                    data.currMove = data.solution[data.i]
                    makeMoves(c, [data.currMove])
                    data.i += 1
                except: print("out of range", data.i, len(data.solution))
        if data.board == data.solved:
            print("yeah")
            data.isSolved = True
            data.currMove = None
            data.solution = None
            data.canSolve = False
            data.i = 0
        else:
            print("No")
            data.isSolved = False
            print(data.board)
        if data.fastSolve:
            data.speed = 2
        else:
            data.speed = 20
    if data.prevMove:
        data.i -= 1
        makeMoves(c, reverseAlg([data.currMove]))
        data.currMove = data.solution[data.i]
        data.prevMove = False


def redrawAll(canvas, data):
    for i in range(len(data.colors)):
        canvas.create_rectangle(i*data.colorWidth, 0, (i+1)*data.colorWidth,
                                data.colorHeight, fill=data.colors[i])
        if data.selectedColor == data.colors[i]:
            canvas.create_rectangle(i*data.colorWidth, 0, (i+1)*data.colorWidth,
                        data.colorHeight, fill=data.colors[i], width=3)
    # print(data.board)
    i = 0
    h = data.cubeHeight
    for face in range(len(data.board)):
        for row in range(len(data.board[0])):
            for col in range(len(data.board[0][0])):
                if face == 0:
                    canvas.create_rectangle((col+3)*data.stickerSize, h +
                        (row-3)*data.stickerSize, (col+4)*data.stickerSize, h +
                        (row-2)*data.stickerSize, fill=data.board[face][row][col])
                elif face == 5:
                    canvas.create_rectangle((col + 3) * data.stickerSize,
                                            h + (row + 3) * data.stickerSize,
                                            (col+ 4) * data.stickerSize,
                                            h + (row + 4) * data.stickerSize,
                                            fill=data.board[face][row][col])
                else:
                    canvas.create_rectangle((col+i-3)*data.stickerSize, h +
                        row*data.stickerSize, (col+i+1-3)*data.stickerSize, h
                    + (row+1)*data.stickerSize, fill=data.board[face][row][col])

                if col == 0:
                    canvas.create_line((col+i-3)*data.stickerSize, h,
                    (col+i-3)*data.stickerSize, h + (row+1)*data.stickerSize,
                                       width=3)
                elif face == 4 and col == 2:
                    canvas.create_line((col + i - 2) * data.stickerSize, h,
                                       (col + i - 2) * data.stickerSize,
                                       h + (row + 1) * data.stickerSize,
                                       width=3)
            if row == 0:
                canvas.create_line(0, h+row*data.stickerSize, data.width,
                                   h+row*data.stickerSize, width=3)
            elif row == 2:
                canvas.create_line(0, h + (row+1) * data.stickerSize, data.width,
                                   h + (row+1) * data.stickerSize, width=3)
        i += 3
    canvas.create_rectangle(3 * data.stickerSize, h - 3 * data.stickerSize,
                            6 * data.stickerSize, h, width=3)
    canvas.create_rectangle(3 * data.stickerSize, h + 3 * data.stickerSize,
                            6 * data.stickerSize, h + 6 * data.stickerSize,
                            width=3)
    x = data.width - 3*data.stickerSize
    canvas.create_rectangle(x, 7*data.height/8, 0.95*data.width,
                            0.95*data.height, fill="black")
    canvas.create_text(0.5*(0.95*data.width + x), (7*data.height/8 +
                        0.95*data.height)/2, text="Solve",
                        fill="white", font="Ariel %d" % (data.width//24))
    canvas.create_rectangle(x, 6*data.height/8, 0.95*data.width,
                            6*data.height/8 + 0.075*data.height, fill="black")
    canvas.create_text(0.5*(0.95*data.width + x), 0.5*(1.5*data.height +
                        0.075*data.height), text="Scramble",
                        fill="white", font="Ariel %d" % (data.width//24))
    if data.scramble != None:
        canvas.create_text(x, data.colorHeight + 2*data.stickerSize -
                           data.height/24, text="Scramble Algorithm:")
        canvas.create_text(x, data.colorHeight + 2*data.stickerSize,
                           text=",".join(data.scramble[:12]).replace(",", "  "))
        canvas.create_text(x, data.colorHeight + 2*data.stickerSize + data.height/30,
                           text=",".join(data.scramble[12:]).replace(",", "  "))
        # print(data.scramble)
    if data.isSolved:
        canvas.create_text(x, data.colorHeight + 2*data.stickerSize,
                        text="Solved!", font="Ariel %d" % (data.width//10))
    drawButtons(canvas, data)


def drawButtons(canvas, data):
    if data.currMove != None:
        x = data.width - 3*data.stickerSize
        canvas.create_text(x, data.colorHeight + 2*data.stickerSize,
                        text="Current Move: %s" % str(data.solution[data.i]),
                        font="Ariel %d" % (data.width//20))
        buttonSize = data.width//30
        canvas.create_oval(x-buttonSize, data.colorHeight + 3*data.stickerSize
                           - buttonSize, x+buttonSize, data.colorHeight +
                           3*data.stickerSize + buttonSize, fill="black")
        if not data.pause:
            canvas.create_line(x-0.4*buttonSize, data.colorHeight + 3*data.stickerSize
                               - buttonSize + 15, x-0.4*buttonSize,
                               data.colorHeight + 3*data.stickerSize +
                               buttonSize - 15, width=8, fill="white")
            canvas.create_line(x + 0.4*buttonSize,
                               data.colorHeight + 3 * data.stickerSize
                               - buttonSize + 15, x + 0.4*buttonSize,
                               data.colorHeight + 3 * data.stickerSize +
                               buttonSize - 15, width=8, fill="white")
        else:
            coordinates = [x-data.width/80, data.colorHeight+3*data.stickerSize
                           - data.width/50, x+data.width/40, data.colorHeight +
                           3*data.stickerSize, x-data.width/80, data.colorHeight
                           + 3*data.stickerSize+data.width/50]
            canvas.create_polygon(coordinates, fill="white")
        nextX = x + 1.5*data.stickerSize
        canvas.create_oval(nextX - buttonSize,
                           data.colorHeight + 3 * data.stickerSize
                           - buttonSize, nextX + buttonSize, data.colorHeight +
                           3 * data.stickerSize + buttonSize, fill="black")
        nextCoord = [nextX - data.width / 60,
                       data.colorHeight + 3 * data.stickerSize
                       - data.width / 60, nextX + data.width/40 - data.width / 60,
                       data.colorHeight +
                       3 * data.stickerSize, nextX - data.width / 60,
                       data.colorHeight
                       + 3 * data.stickerSize + data.width / 60]
        canvas.create_polygon(nextCoord, fill="white")
        nextCoord2 = [nextX,
                     data.colorHeight + 3 * data.stickerSize
                     - data.width / 60, nextX + data.width / 40,
                     data.colorHeight +
                     3 * data.stickerSize, nextX,
                     data.colorHeight
                     + 3 * data.stickerSize + data.width / 60]
        canvas.create_polygon(nextCoord2, fill="white")
        prevX = x - 1.5*data.stickerSize
        canvas.create_oval(prevX - buttonSize,
                           data.colorHeight + 3 * data.stickerSize
                           - buttonSize, prevX + buttonSize, data.colorHeight +
                           3 * data.stickerSize + buttonSize, fill="black")
        canvas.create_text(prevX, data.colorHeight+3*data.stickerSize - 5, text="<",
                           font=("Ariel", data.width//20, 'bold'), fill="white")


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

run(800, 800)
