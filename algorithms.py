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
moveList = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'",
                "D2", "F", "F'", "F2", "B", "B'", "B2"]
colorToFace = {"yellow": 0, "red": 1, "green": 2, "orange": 3, "blue": 4,
               "white": 5}
faceToColor = {0: "yellow", 1: "red", 2: "green", 3: "orange", 4: "blue",
               5: "white"}
moves = []

def getColorEdges(edges, colors, color):
    # returns a list of the edges with color color in the solved state
    # edges never change
    c = colors[color]
    edgeList = []
    for edge in edges:
        if len(edge & c) != 0:
            edgeList.append(edge)
    return edgeList

def getLocation(piece, cube, edges, corners):
    # use Moves.getListCube() to turn cube into a list
    # returns a list of the locations of the pieces in the current cube
    if not isinstance(cube, list):
        cube = cube.getListCube()
    location = []
    for face in range(len(cube)):
        for row in range(len(cube[0])):
            for col in range(len(cube[0][0])):
                if cube[face][row][col] in piece:
                    location.append([face, row, col])
                    if piece in edges:
                        if len(location) == 2:
                            if cube[location[0][0]][location[0][1]][location[0][2]] in range(9):
                                return location
                            else:
                                return location.reverse()
                    elif piece in corners:
                        if len(location) == 3:
                            return location
    return location

def edgeLocations(colorEdges, cube, edges, corners):
    # returns the locations of all the edges of one color
    edgeLoc = []
    for edge in colorEdges:
        edgeLoc.append(getLocation(edge, cube, edges, corners))
    return edgeLoc

whiteEdges = getColorEdges(edges, colors, "white")
def solveCross(moveCube, whiteEdges, colors):
    # solves the white cross
    cube = moveCube.getListCube()
    moves = []
    for edge in whiteEdges:
        if edge[0] in colors["white"]:
            white = edge[0]
            otherColor = edge[1]
        else:
            white = edge[1]
            otherColor = edge[0]
        location = getLocation(edge, cube, edges, corners)
        moves.extend(putOnBottom(moveCube, [white, otherColor], location, colors))
    return moves

def alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors):
    # put the white piece on the top then use put on bottom after
    moves = []
    cube = moveCube.getListCube()
    f, r, c = otherLoc
    otherC = None
    for color in colors:
        if cube[f][r][c] in colors[color]:
            otherC = color
            break
    if otherC == None:
        return "Cannot be Solved"
    if whiteLocation[0] == 0:
        # is on top
        while otherLoc[0] != colorToFace[otherC]:
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation([whiteNum, otherNum], moveCube, edges, corners)
            whiteLocation, otherLoc = l
    elif whiteLocation[0] == 1:
        while whiteLocation != 0:
            if otherLoc[0] == 0:
                pass
    elif whiteLocation[0] == 2:
        # move to top
        while whiteLocation[0] != 0:
            if otherLoc[0] == 0:
                moves.extend(makeMoves(moveCube, ["F", "R", "U'", "R'"]))
            elif otherLoc[0] == 1:
                moves.extend(makeMoves(moveCube, ["L'", "U'", "L"]))
            elif otherLoc[0] == 3:
                moves.extend(makeMoves(moveCube, ["R", "U", "R'"]))
            elif otherLoc[0] == 5:
                moves.extend(makeMoves(moveCube, ["F'", "R", "U'", "R'"]))
            l = getLocation([whiteNum, otherNum], moveCube, edges, corners)
            whiteLocation, otherloc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors)


    elif whiteLocation[0] == 5:
        # move to top
        moves.extend(moveCube.turnFace(f) * 2)
        l = getLocation([whiteNum, otherNum], moveCube, edges, corners)
        whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors)
    return moves





def putOnBottom(moveCube, edge, location, colors):
    moves = []
    white, otherColor = edge
    whiteLocation = location[0]
    otherLoc = location[1]
    moves.extend(alignEdge(moveCube, white, otherColor, whiteLocation, otherLoc, colors))
    moves.extend(solveTheCross(moveCube, moveList))
    return moves


def solveTheCross(moveCube, moveList):
    moves = []
    for move in moveList:
        moves.extend(makeMoves(moveCube, [move]))
        cube = moveCube.getListCube()
        if cube[5][0][1] == 46 and cube[5][1][0] == 48 and cube[5][1][2] == 50 \
                                    and cube[5][2][1] == 52:
            return moves
        moves.extend(makeMoves(moveCube, reverseAlg([move])))
    return moves




















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


def solveWhiteCross(moveCube, edges, colors):
    whiteEdges = getColorEdges(edges, colors, "white")
    locations = edgeLocations(whiteEdges, moveCube, edges, corners)
    if not isinstance(moveCube, Cube):
        moveCube = Cube(moveCube)
    c = moveCube.getListCube()
    m = []
    for edge in locations:
        face1, row1, col1 = edge[0][0], edge[0][1], edge[0][2]
        face2, row2, col2 = edge[1][0], edge[1][1], edge[1][2]
        if c[face1][row1][col1] not in colors["white"]:
            face1, row1, col1, face2, row2, col2 = face2, row2, col2, face1, \
                                                   row1, col1
        if face1 == 0:
            m.extend(whiteOnTop(moveCube, row1, col1))




        c = moveCube.getListCube()

    return m

def getColor(cube, frc, colors):
    # returns the color of the sticker at the specific face, row, and col
    # cube is a Cube type
    f, r, c = frc
    for color in colors:
        if cube.getListCube()[f][r][c] in colors[color]:
            return color



#
#
# def solveTheCross(moveCube, edges, colors):
#     whiteEdges = getColorEdges(edges, colors, "white")
#     unsolvedCrossColors = ["green", "orange", "blue", "red"]
#     return solveCross(moveCube, edges, colors, whiteEdges, unsolvedCrossColors)
#
# def solveCross(moveCube, edges, colors, whiteEdges, unsolvedCrossColors):
#     whiteLocations = edgeLocations(whiteEdges, moveCube, edges, corners)
#     faceTurnMap = {"white": ["D", "D'", "D2"], "yellow": ["U", "U'", "U2"],
#                    "red": ["L", "L'", "L2"], "green": ["F", "F'", "F2"],
#                    "orange": ["R", "R'", "R2"], "blue": ["B", "B'", "B2"]}
#     if isSolvedCross(moveCube):
#         return moveCube
#     cube = moveCube.getListCube()
#     for color in unsolvedCrossColors:
#         for edge in whiteLocations:
#             for side in edge:
#                 f, r, c = side
#                 if getColor(moveCube, edge, colors) == color:
#                     if cube[f][r][c] in colors[color]:
#                         # side of the edge is on the color face
#                         for move in faceTurnMap[color]:
#                             moveCube = makeMove(moveCube, [move])
#                             if moveCube.getListCube()
#                                 # check that the piece is in the right place
#                                 # need location of the piece
#                                 tmpSoln = solveCross(moveCube, edges, colors,
#                                             whiteEdges, unsolvedCrossColors[1:])
#                                 if tmpSoln != None:
#                                     return tmpSoln
#                             moveCube = makeMove(moveCube, reverseAlg(moveCube, [move]))
#                     else:
#                         if cube[f][r][c]

#
#                         pass
#
#                         # make moves until piece is in bottom
#                         # need to check that
#



def isSolvedCross(moveCube):
    cube = moveCube.getListCube()
    return cube[5][0][1] == 46 and cube[5][1][0] == 48 and cube[5][1][2] == 50 \
            and cube[5][2][1] == 52




