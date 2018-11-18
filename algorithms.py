from rubikMoves import *
from scrambler import *
"""contains all the steps to solve the cube"""

edges = [{7,19}, {14,21}, {23,30}, {25,46}, {5,28}, {3,10}, {1,37}, {32,39},
         {34,50}, {43,52}, {41,12}, {16,48}]
corners = [{6,11,18}, {8,20,27}, {17,24,45}, {26,33,47}, {2,29,36}, {35,42,47},
           {15,44,51}, {0,9,38}]
colors = {"yellow": set(range(9)), "red": set(range(9, 18)), "green":
            set(range(18, 27)), "orange": set(range(27, 36)), "blue":
            set(range(36, 45)), "white": set(range(45, 54))}

def getColorEdges(edges, colors, color):
    # returns a list of the edges with color color in the solved state
    c = colors[color]
    edgeList = []
    for edge in edges:
        if len(edge & c) != 0:
            edgeList.append(edge)
    return edgeList

def getLocation(piece, cube, edges, corners):
    # use Moves.getListCube() to turn cube into a list
    location = []
    for face in range(len(cube)):
        for row in range(len(cube[0])):
            for col in range(len(cube[0][0])):
                if cube[face][row][col] in piece:
                    location.append([face, row, col])
                    if piece in edges:
                        if len(location) == 2:
                            return location
                    elif piece in corners:
                        if len(location) == 3:
                            return location

def edgeLocations(colorEdges, cube, edges, corners):
    edgeLoc = []
    for edge in colorEdges:
        edgeLoc.append(getLocation(edge, cube, edges, corners))
    return edgeLoc

def whiteOnTop(moveCube, row, col):
    # moves white edge on the upper face to the down face

    ##### work on moving the second color over the actual location
    move = []
    if row == 0:
        moveCube.turnBack()
        moveCube.turnBack()
        move = ["B2"]
    elif row == 1:
        if col == 0:
            moveCube.turnLeft()
            moveCube.turnLeft()
            move = ["L2"]
        elif col == 2:
            moveCube.turnRight()
            moveCube.turnRight()
            move = ["R2"]
    elif row == 2:
        moveCube.turnFront()
        moveCube.turnFront()
        move = ["F2"]
    return move


def solveWhiteCross(cube, edges, colors):
    whiteEdges = getColorEdges(edges, colors, "white")
    locations = edgeLocations(whiteEdges, cube, edges, corners)
    moveCube = Cube(cube)
    m = []
    for edge in locations:
        face1, row1, col1 = edge[0][0], edge[0][1], edge[0][2]
        face2, row2, col2 = edge[1][0], edge[1][1], edge[1][2]
        if cube[face1][row1][col1] not in colors["white"]:
            face1, row1, col1, face2, row2, col2 = face2, row2, col2, face1, \
                                                   row1, col1
        if face1 == 0:
            m.extend(whiteOnTop(moveCube, row1, col1))





        cube = moveCube.getListCube()




    return m




