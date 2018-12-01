# import everything from rubikMoves
from rubikMoves import *
from RubiksCube import *

""" This file contains the Rubik's Cube animation functions and also converts 
the animated Rubik's Cube into a 3D list of numbers that will be used to find 
the solution to the puzzle"""

colors = {"yellow": set(range(9)), "red": set(range(9, 18)), "green":
            set(range(18, 27)), "orange": set(range(27, 36)), "blue":
            set(range(36, 45)), "white": set(range(45, 54))}

def convertBoardToCube(board):

    c = [[[None for k in range(3)] for i in range(3)] for j in range(6)]
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
    print("scrambleCube", scramble)
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


# animation template from
# https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
from tkinter import *
def init(data):
    data.colors = ["yellow", "red", "green", "orange", "blue", "white"]
    data.board = [[["grey" for k in range(3)] for j in range(3)] for i in range(6)]
    for face in range(len(data.board)):
        # initialize the center colors
        data.board[face][1][1] = data.colors[face]
    data.selectedColor = "white"
    data.colorWidth = data.width/6
    data.colorHeight = data.height/10
    data.stickerSize = data.width/12
    data.cubeHeight = data.height/3 + data.colorHeight
    data.canSolve = False
    data.scramble = None
    data.solution = None
    data.time = 0
    data.i = 0
    data.currMove = None
    data.isSolved = False
    data.solving = False
    data.solved = [[[color for i in range(3)] for j in range(3)] for color in colors]
    data.pause = False
    data.fastSolve = False
    data.speed = 15
    data.prevMove = False
    data.cubeSize = min(data.width, data.height) / 3
    data.start = True
    data.view = True
    data.showCannotSolve = False

def inputPress(event, data):
    if 0 <= event.y <= data.colorHeight:
        for i in range(6):
            if i * data.colorWidth <= event.x < (i + 1) * data.colorWidth:
                data.selectedColor = data.colors[i]
    h = data.cubeHeight
    if data.view:
        if data.cubeHeight <= event.y < data.cubeHeight + 3 * data.stickerSize:
            i = 0

            for face in range(len(data.board)):
                for row in range(len(data.board[0])):
                    for col in range(len(data.board[0][0])):
                        if (col + i - 3) * data.stickerSize <= event.x <= (
                                col + i - 2) * data.stickerSize:
                            if h + row * data.stickerSize <= event.y <= h + (
                                    row + 1) * data.stickerSize:
                                data.board[face][row][col] = data.selectedColor
                i += 3
        elif 3 * data.stickerSize <= event.x < 6 * data.stickerSize:
            # data.cubeHeight - 3*data.stickerSize <= event.y < data.cubeHeight:

            # for face in [0, 5]:
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if (col + 3) * data.stickerSize <= event.x < (
                            col + 4) * data.stickerSize:
                        if h + (row - 3) * data.stickerSize <= event.y < h + (
                                row - 2) * data.stickerSize:
                            data.board[0][row][col] = data.selectedColor
                        elif h + (row + 3) * data.stickerSize <= event.y < h + (
                                row + 4) * data.stickerSize:
                            data.board[5][row][col] = data.selectedColor
    else:
        if h <= event.y < h + 3 * data.stickerSize:
            i = 0
            h = data.cubeHeight
            for face in [1, 2]:
                for row in range(len(data.board[0])):
                    for col in range(len(data.board[0][0])):
                        if (col + i) * data.stickerSize <= event.x <= (
                                col + i + 1) * data.stickerSize:
                            if h + row * data.stickerSize <= event.y <= h + (
                                    row + 1) * data.stickerSize:
                                data.board[face][row][col] = data.selectedColor
                i += 3
        elif 3 * data.stickerSize <= event.x < 6 * data.stickerSize:
            # data.cubeHeight - 3*data.stickerSize <= event.y < data.cubeHeight:
            h = data.cubeHeight
            # for face in [0, 5]:
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if (col + 3) * data.stickerSize <= event.x < (
                            col + 4) * data.stickerSize:
                        if h + (row + 3) * data.stickerSize <= event.y < h + (
                                row + 4) * data.stickerSize:
                            data.board[5][row][col] = data.selectedColor

        cubeSize = 3*data.stickerSize
        cubeTrig = 0.5 * 2**0.5 * cubeSize
        if 2*cubeSize <= event.x < 2*cubeSize + cubeTrig:
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if h + row*data.stickerSize - event.x + 2*cubeSize <= \
                                event.y < h + (row+1)*data.stickerSize - \
                                event.x + 2*cubeSize:
                        if 2*cubeSize + col*cubeTrig/3 <= event.x < \
                                2*cubeSize + (col+1)*cubeTrig/3:
                                    data.board[3][row][col] = data.selectedColor

        if h - cubeTrig <= event.y < h:
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if cubeSize + cubeTrig - row*cubeTrig/3 - event.y + h - \
                            cubeTrig + row*cubeTrig/3 + col*data.stickerSize <= \
                            event.x < cubeSize + cubeTrig - row*cubeTrig/3 - \
                            event.y + h - cubeTrig + row*cubeTrig/3 + \
                            (col+1)*data.stickerSize:
                        if h - cubeTrig + row*cubeTrig/3 <= event.y < \
                                h - cubeTrig + (row+1) * cubeTrig / 3:
                            data.board[0][row][col] = data.selectedColor
        if 2*cubeSize + cubeTrig <= event.x < 3*cubeSize + cubeTrig \
                and h - cubeTrig <= event.y < h - cubeTrig + cubeSize:
            for row in range(len(data.board[0])):
                for col in range(len(data.board[0][0])):
                    if 2*cubeSize + cubeTrig + col*data.stickerSize <= \
                            event.x < 2*cubeSize + cubeTrig + \
                            (col+1)*data.stickerSize:
                        if h - cubeTrig + row*data.stickerSize <= event.y < \
                                h - cubeTrig + (row+1)*data.stickerSize:
                            data.board[4][row][col] = data.selectedColor

def mousePressed(event, data):
    if data.start and data.width/4 <= event.x < 3*data.width/4 and \
            3*data.height/4 <= event.y < 7*data.height/8:
        data.start = False
    else:
        if not data.solving:
            inputPress(event, data)
            if data.width - 3*data.stickerSize <= event.x < 0.95*data.width and \
                6*data.height/8 <= event.y < 6*data.height/8 + 0.075*data.height:
                data.scramble = scrambleAlgorithm()
                r = randomScramble(data.scramble)
                c = cubeToBoard(r, colors)
                # print(c)
                data.board = c
            elif data.width - 3*data.stickerSize <= event.x < 0.95*data.width and \
                            7*data.height/8 <= event.y < 0.95*data.height:
                print("Solving...")
                if data.canSolve:
                    c = convertBoardToCube(data.board)
                    print("c is", c)
                    try:
                        data.solution = solveCube(c)
                        data.solving = True
                        data.scramble = None
                    except:
                        data.showCannotSolve = True
                        print("Cube is Unsolvable")
                else:
                    data.showCannotSolve = True
                    print("Cube is Unsolvable")
        if 0.05*data.width <= event.x < 0.16*data.width and \
                7 * data.height / 8 <= event.y < 0.95*data.height:
            init(data)
            data.start = False
        elif 0.05 * data.width <= event.x < 0.16 * data.width and \
            3 * data.height/4 <= event.y < 0.95 * data.height - data.height/8:
            data.view = not data.view
        else:
            pauseX = data.width - 3*data.stickerSize
            pauseY = data.colorHeight + data.stickerSize
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
        data.start = False

def timerFired(data):
    c = Cube(data.board)
    count = 0
    i = 0
    for face in data.board:
        for row in face:
            if "grey" in row:
                data.canSolve = False
                break
            else:
                count += 1
            i += 1
    if count == i:
        data.canSolve = True
    if not data.pause:
        data.time += 1
        if data.solution != None:
            data.board = c.cube
            if data.time % data.speed == 0:
                try:
                    data.currMove = data.solution[data.i]
                    makeMoves(c, [data.currMove])
                    data.i += 1
                except:
                    print("out of range", data.i, len(data.solution))
                    if not data.isSolved:
                        data.i = 0
                        print("not solved", c)
                        cube = convertBoardToCube(data.board)
                        yellowCorners = getColorCorners(colors, "yellow")
                        data.solution = orientYellowCorners(cube, yellowCorners)
                        makeMoves(cube, data.solution)
                        print("made extra moves")
        if data.board == data.solved:
            data.isSolved = True
            data.currMove = None
            data.solution = None
            # data.canSolve = False
            data.solving = False
            data.i = 0
        else:
            # print("No")
            data.isSolved = False
            # print(data.board)
        if data.fastSolve:
            data.speed = 0.25
        else:
            data.speed = 15
        if data.showCannotSolve:
            if data.time % 20 == 0:
                data.showCannotSolve = False
    if data.prevMove:
        data.pause = True
        if data.i > 1:
            data.i -= 1
            data.currMove = data.solution[data.i]
            makeMoves(c, reverseAlg([data.currMove]))
        data.prevMove = False


def redrawAll(canvas, data):
    if data.start:
        drawStartScreen(canvas, data)
    else:
        if not data.solving:
            drawColorPalette(canvas, data)
        if data.view:
            drawCubeLayout(canvas, data)
        else:
            draw3DCube(canvas, data)
        drawScramble(canvas, data)
        if data.isSolved:
            canvas.create_text(data.width - 3 * data.stickerSize,
                            data.colorHeight + data.stickerSize,
                            text="Solved!", font="Ariel %d" % (data.width//10))
        drawButtons(canvas, data)

        if data.showCannotSolve:
            canvas.create_rectangle(0, data.height/2 - data.stickerSize,
                        data.width, data.height/2 + data.stickerSize, fill="black")
            canvas.create_text(data.width / 2, data.height / 2,
                    text="Cube is Unsolvable!", font="Ariel %d" %
                                        (data.width // 10), fill="white")



def drawColorPalette(canvas, data):
    for i in range(len(data.colors)):
        canvas.create_rectangle(i * data.colorWidth, 0,
                                (i + 1) * data.colorWidth,
                                data.colorHeight, fill=data.colors[i])
        if data.selectedColor == data.colors[i]:
            canvas.create_rectangle(i * data.colorWidth, 0,
                                    (i + 1) * data.colorWidth,
                                    data.colorHeight, fill=data.colors[i],
                                    width=3)

def drawCubeLayout(canvas, data):
    i = 0
    h = data.cubeHeight
    for face in range(len(data.board)):
        for row in range(len(data.board[0])):
            for col in range(len(data.board[0][0])):
                if face == 0:
                    canvas.create_rectangle((col + 3) * data.stickerSize, h +
                                            (row - 3) * data.stickerSize,
                                            (col + 4) * data.stickerSize, h +
                                            (row - 2) * data.stickerSize,
                                            fill=data.board[face][row][col])
                elif face == 5:
                    canvas.create_rectangle((col + 3) * data.stickerSize,
                                            h + (row + 3) * data.stickerSize,
                                            (col + 4) * data.stickerSize,
                                            h + (row + 4) * data.stickerSize,
                                            fill=data.board[face][row][col])
                else:
                    canvas.create_rectangle((col + i - 3) * data.stickerSize,
                                            h +
                                            row * data.stickerSize, (
                                                        col + i + 1 - 3) * data.stickerSize,
                                            h
                                            + (row + 1) * data.stickerSize,
                                            fill=data.board[face][row][col])

                if col == 0:
                    canvas.create_line((col + i - 3) * data.stickerSize, h,
                                       (col + i - 3) * data.stickerSize,
                                       h + (row + 1) * data.stickerSize,
                                       width=3)
                elif face == 4 and col == 2:
                    canvas.create_line((col + i - 2) * data.stickerSize, h,
                                       (col + i - 2) * data.stickerSize,
                                       h + (row + 1) * data.stickerSize,
                                       width=3)
            if row == 0:
                canvas.create_line(0, h + row * data.stickerSize, data.width,
                                   h + row * data.stickerSize, width=3)
            elif row == 2:
                canvas.create_line(0, h + (row + 1) * data.stickerSize,
                                   data.width,
                                   h + (row + 1) * data.stickerSize, width=3)
        i += 3
    canvas.create_rectangle(3 * data.stickerSize, h - 3 * data.stickerSize,
                            6 * data.stickerSize, h, width=3)
    canvas.create_rectangle(3 * data.stickerSize, h + 3 * data.stickerSize,
                            6 * data.stickerSize, h + 6 * data.stickerSize,
                            width=3)

def draw3DCube(canvas, data):
    h = data.cubeHeight
    i = 0
    offTop = 0
    cubeSize = 3 * data.stickerSize
    stickerMove = data.stickerSize * 0.5 * 2 ** 0.5
    cubeTrig = 0.5 * cubeSize * 2 ** 0.5
    verticalSticker = cubeTrig / 3
    for face in range(len(data.board)):
        for row in range(len(data.board[0])):
            offUp = 0
            for col in range(len(data.board[0][0])):
                if face == 5:
                    canvas.create_rectangle((col + 3) * data.stickerSize,
                                            h + (row + 3) * data.stickerSize,
                                            (col + 4) * data.stickerSize,
                                            h + (row + 4) * data.stickerSize,
                                            fill=data.board[face][row][col])
                elif face in [1, 2]:
                    canvas.create_rectangle((col + i - 3) * data.stickerSize,
                                            h +
                                            row * data.stickerSize, (
                                            col + i - 2) * data.stickerSize,
                                            h + (row + 1) * data.stickerSize,
                                            fill=data.board[face][row][col])

                elif face == 0:

                    if row == col == 0:
                        canvas.create_polygon(cubeSize, h, cubeSize+cubeTrig,
                                        h - cubeTrig, 2*cubeSize + cubeTrig,
                                        h - cubeTrig, 2*cubeSize, h, width=4,
                                              outline="black")

                    points = [cubeSize + cubeTrig + col*data.stickerSize -
                        offTop, h - cubeTrig + row*verticalSticker,
                        cubeSize + cubeTrig + (col+1)*data.stickerSize - offTop,
                        h - cubeTrig + row*verticalSticker,
                        cubeSize + cubeTrig + (col+1)*data.stickerSize -
                        stickerMove - offTop, h - cubeTrig + (row+1)
                        * verticalSticker, cubeSize + cubeTrig +
                        col*data.stickerSize - stickerMove - offTop,
                        h - cubeTrig + (row+1)*verticalSticker]
                    canvas.create_polygon(points, fill=data.board[face][row][col],
                            outline="black", width=1)
                elif face == 3:
                    if row == col == 0:
                        canvas.create_polygon(2*cubeSize, h, 2*cubeSize +
                                cubeTrig, h - cubeTrig, 2*cubeSize + cubeTrig,
                                h + cubeSize - cubeTrig, 2*cubeSize,
                                h + cubeSize, width=3, outline="black")
                    points = [2*cubeSize + col*verticalSticker,
                            h + row*data.stickerSize - offUp, 2*cubeSize + (col+1)
                            * verticalSticker, h + row *
                            data.stickerSize - stickerMove - offUp,
                            2*cubeSize + (col+1) * verticalSticker,
                            h + (row+1)*data.stickerSize - stickerMove - offUp,
                            2*cubeSize + col*verticalSticker,
                                  h + (row+1)*data.stickerSize - offUp
                                  ]
                    canvas.create_polygon(points, outline="black", width=1,
                                              fill=data.board[face][row][col])
                    offUp += stickerMove
                elif face == 4:

                    canvas.create_rectangle(2*cubeSize+cubeTrig +
                                col*data.stickerSize, h - cubeTrig +
                                row*data.stickerSize, 2*cubeSize+cubeTrig +
                                (col+1)*data.stickerSize, h - cubeTrig +
                                (row+1)*data.stickerSize,
                                            fill=data.board[face][row][col])


            if face == 0:
                offTop += stickerMove

        i += 3
    canvas.create_rectangle(2 * cubeSize +
                                        cubeTrig, h - cubeTrig,
                                        3 * cubeSize + cubeTrig,
                                        h + cubeSize - cubeTrig, width=3)
    canvas.create_rectangle(3 * data.stickerSize,
                            h + 3 * data.stickerSize,
                            6 * data.stickerSize,
                            h + 6 * data.stickerSize, width=3)
    canvas.create_rectangle(0, h, cubeSize, h + cubeSize, width=3)
    canvas.create_rectangle(cubeSize, h, 2*cubeSize, h+cubeSize, width=3)
    canvas.create_line(2 * cubeSize, h + cubeSize, 2 * cubeSize + cubeTrig,
                       h + cubeSize - cubeTrig, width=3)
    canvas.create_line(2*cubeSize, h, 2*cubeSize+cubeTrig,
                       h-cubeTrig, width=3)

def drawScramble(canvas, data):
    if data.scramble != None:
        x = data.width - 3 * data.stickerSize
        canvas.create_text(x, data.colorHeight + 2 * data.stickerSize -
                           data.height / 24, text="Scramble Algorithm:",
                           font=("Ariel", data.width // 30))
        canvas.create_text(x, data.colorHeight + 2 * data.stickerSize,
                           text=",".join(data.scramble[:12]).replace(",", "  "),
                           font=("Ariel", data.width // 40))
        canvas.create_text(x, data.colorHeight + 2 * data.stickerSize +
                           data.height / 30,
                           text=",".join(data.scramble[12:]).replace(",", "  "),
                           font=("Ariel", data.width // 40))

def drawButtons(canvas, data):
    x = data.width - 3 * data.stickerSize
    if not data.solving:
        canvas.create_rectangle(x, 7 * data.height / 8, 0.95 * data.width,
                                0.95 * data.height, fill="black")
        canvas.create_text(0.5 * (0.95 * data.width + x), (7 * data.height / 8 +
                                                           0.95 * data.height) / 2,
                           text="Solve",
                           fill="white", font="Ariel %d" % (data.width // 24))
        canvas.create_rectangle(x, 6 * data.height / 8, 0.95 * data.width,
                                6 * data.height / 8 + 0.075 * data.height,
                                fill="black")
        canvas.create_text(0.5 * (0.95 * data.width + x), 0.5 * (1.5 * data.height +
                                                                 0.075 * data.height),
                           text="Scramble",
                           fill="white", font="Ariel %d" % (data.width // 24))
    canvas.create_rectangle(0.05*data.width, 7*data.height/8, 0.16*data.width,
                            0.95*data.height, fill="black")
    canvas.create_text(0.105*data.width, 0.9125*data.height, text="Reset",
                       fill="white", font=("Ariel", data.width//24))
    canvas.create_rectangle(0.05 * data.width, 3 * data.height / 4,
                        0.16 * data.width, 0.95 * data.height - data.height/8,
                            fill="black")
    canvas.create_text(0.105 * data.width, 0.9125 * data.height - data.height/8,
                    text="View", fill="white", font=("Ariel", data.width // 24))

    if data.currMove != None:
        x = data.width - 3*data.stickerSize
        canvas.create_text(x, data.colorHeight,
                        text="Current Move: %s %d" % (str(data.solution[data.i-1]), data.i),
                        font="Ariel %d" % (data.width//20))
        buttonSize = data.width//30
        canvas.create_oval(x-buttonSize, data.colorHeight + data.stickerSize
                           - buttonSize, x+buttonSize, data.colorHeight +
                           data.stickerSize + buttonSize, fill="black")
        if not data.pause:
            canvas.create_line(x-0.4*buttonSize, data.colorHeight + data.stickerSize
                               - buttonSize + 15, x-0.4*buttonSize,
                               data.colorHeight + data.stickerSize +
                               buttonSize - 15, width=8, fill="white")
            canvas.create_line(x + 0.4*buttonSize,
                               data.colorHeight + data.stickerSize
                               - buttonSize + 15, x + 0.4*buttonSize,
                               data.colorHeight + data.stickerSize +
                               buttonSize - 15, width=8, fill="white")
        else:
            coordinates = [x-data.width/80, data.colorHeight+data.stickerSize
                           - data.width/50, x+data.width/40, data.colorHeight +
                           data.stickerSize, x-data.width/80, data.colorHeight
                           + data.stickerSize+data.width/50]
            canvas.create_polygon(coordinates, fill="white")
        nextX = x + 1.5*data.stickerSize
        canvas.create_oval(nextX - buttonSize,
                           data.colorHeight + data.stickerSize
                           - buttonSize, nextX + buttonSize, data.colorHeight +
                           data.stickerSize + buttonSize, fill="black")
        nextCoord = [nextX - data.width / 60,
                       data.colorHeight + data.stickerSize
                       - data.width / 60, nextX + data.width/40 - data.width / 60,
                       data.colorHeight +
                       data.stickerSize, nextX - data.width / 60,
                       data.colorHeight +
                       data.stickerSize + data.width / 60]
        canvas.create_polygon(nextCoord, fill="white")
        nextCoord2 = [nextX,
                     data.colorHeight + data.stickerSize
                     - data.width / 60, nextX + data.width / 40,
                     data.colorHeight +
                      data.stickerSize, nextX,
                     data.colorHeight
                     + data.stickerSize + data.width / 60]
        canvas.create_polygon(nextCoord2, fill="white")
        prevX = x - 1.5*data.stickerSize
        canvas.create_oval(prevX - buttonSize,
                           data.colorHeight + data.stickerSize
                           - buttonSize, prevX + buttonSize, data.colorHeight +
                           data.stickerSize + buttonSize, fill="black")
        canvas.create_text(prevX, data.colorHeight+data.stickerSize - 5, text="<",
                           font=("Ariel", data.width//20, 'bold'), fill="white")

def drawStartScreen(canvas, data):
    centeringFactor = data.cubeSize/4
    canvas.create_rectangle(data.cubeSize - centeringFactor, data.cubeSize,
                            2*data.cubeSize - centeringFactor,
                            2*data.cubeSize, fill="white", width=3)
    canvas.create_polygon(data.cubeSize - centeringFactor, data.cubeSize,
                          3*data.cubeSize/2 - centeringFactor, data.cubeSize/2,
                          5*data.cubeSize/2 - centeringFactor,
                          data.cubeSize/2, 2*data.cubeSize - centeringFactor,
                          data.cubeSize, fill="blue", outline="black", width=3)
    canvas.create_polygon(5*data.cubeSize/2 - centeringFactor, data.cubeSize/2,
                        5*data.cubeSize/2 - centeringFactor, 3*data.cubeSize/2,
                        2*data.cubeSize - centeringFactor, 2*data.cubeSize,
                        2*data.cubeSize - centeringFactor,
                          data.cubeSize,fill="red", outline="black", width=3)
    canvas.create_line(data.cubeSize - centeringFactor, 4*data.cubeSize/3,
                       2*data.cubeSize - centeringFactor, 4*data.cubeSize/3, width=3)
    canvas.create_line(data.cubeSize - centeringFactor, 5*data.cubeSize/3,
                       2*data.cubeSize - centeringFactor, 5*data.cubeSize/3, width=3)
    canvas.create_line(4*data.cubeSize/3 - centeringFactor, data.cubeSize,
                       4*data.cubeSize/3 - centeringFactor, 2*data.cubeSize, width=3)
    canvas.create_line(5*data.cubeSize/3 - centeringFactor, data.cubeSize,
                       5*data.cubeSize/3 - centeringFactor, 2*data.cubeSize, width=3)
    canvas.create_line(4*data.cubeSize/3 - centeringFactor, data.cubeSize,
                       11*data.cubeSize/6- centeringFactor, data.cubeSize/2, width=3)
    canvas.create_line(5 * data.cubeSize/3 - centeringFactor, data.cubeSize,
                       13 * data.cubeSize/6 - centeringFactor, data.cubeSize/2, width=3)
    canvas.create_line(4*data.cubeSize/3 - centeringFactor, 2*data.cubeSize/3,
                       7*data.cubeSize/3 - centeringFactor, 2*data.cubeSize/3, width=3)
    canvas.create_line(7*data.cubeSize/6 - centeringFactor, 5*data.cubeSize/6,
                       13*data.cubeSize/6 - centeringFactor,
                       5*data.cubeSize/6, width=3)
    canvas.create_line(13*data.cubeSize/6 - centeringFactor, 5*data.cubeSize/6,
                       13*data.cubeSize/6 - centeringFactor, 11*data.cubeSize/6, width=3)
    canvas.create_line(7*data.cubeSize/3 - centeringFactor, 2*data.cubeSize/3,
                       7 * data.cubeSize / 3 - centeringFactor,
                       5 * data.cubeSize / 3, width=3)
    canvas.create_line(2*data.cubeSize - centeringFactor, 4*data.cubeSize/3,
                       5*data.cubeSize/2 - centeringFactor, 5*data.cubeSize/6, width=3)
    canvas.create_line(2*data.cubeSize - centeringFactor, 5*data.cubeSize/3,
                       5*data.cubeSize/2 - centeringFactor, 7*data.cubeSize/6, width=3)
    canvas.create_text(data.width/2, data.height/12, text="Rubik's Cube Solver",
                       font=("Ariel", int(data.cubeSize/4), 'bold'))
    canvas.create_rectangle(data.width/4, 6*data.height/8, 3*data.width/4, 7*data.height/8, fill="black")
    canvas.create_text(data.width/2, 13*data.height/16, text="Press To Begin",
                       fill="white", font=("Ariel", int(data.width/16), 'bold'))



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
