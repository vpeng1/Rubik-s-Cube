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
            edgeList.append(list(edge))
    return edgeList

def getLocation(piece, cube, edges, corners, ran = range(45, 54)):
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
                            return checkLocation(cube, location, ran)
                            # print("hello world")
                            # f, r, c = location[0]
                            # if cube[f][r][c] in ran:
                            #     # want first index to be the index for the white side
                            #     return location
                            # else:
                            #     print(piece)
                            #     print("cube", cube)
                            #     location.reverse()
                            #     return location
                    elif piece in corners:
                        if len(location) == 3:
                            return location


def checkLocation(cube, location, rangeValues):
    f, r, c = location[0]
    if cube[f][r][c] not in rangeValues:
        location.reverse()
        return location
    else:
        return location

def testGetLocations():
    print("Testing Get Locations...", end="")
    cube = [[[45, 30, 6], [34, 4, 1], [35, 16, 36]],
            [[17, 50, 53], [5, 13, 46], [27, 14, 47]],
            [[42, 48, 2], [25, 22, 52], [26, 7, 38]],
            [[29, 37, 11], [43, 31, 39], [0, 3, 51]],
            [[18, 23, 24], [32, 40, 28], [44, 12, 8]],
            [[33, 19, 9], [21, 49, 10], [20, 41, 15]]]
    print(getLocation({52, 43}, cube, edges, corners))
    print("Passed!")
testGetLocations()


# def edgeLocations(colorEdges, cube, edges, corners):
#     # returns the locations of all the edges of one color
#     # use getColorEdges
#     edgeLoc = []
#     for edge in colorEdges:
#         edgeLoc.append(getLocation(edge, cube, edges, corners))
#     return edgeLoc

whiteEdges = getColorEdges(edges, colors, "white")
def solveCross(moveCube, whiteEdges, colors):
    # solves the white cross
    moves = []
    for edge in whiteEdges:
        print("solving for edge", edge)
        cube = moveCube.getListCube()
        if edge[0] in colors["white"]:
            white = edge[0]
            otherColor = edge[1]
        else:
            white = edge[1]
            otherColor = edge[0]
        location = getLocation({white, otherColor}, cube, edges, corners)
        moves.extend(putOnBottom(moveCube, [white, otherColor], location, colors))
        print("solve", moves)
        cube = moveCube.getListCube()
    assert(cube[5][0][1] == 46)
    assert(cube[5][1][0] == 48)
    assert(cube[5][1][2] == 50)
    assert(cube[5][2][1] == 52)
    print("PASSED!!!!!!!!!!")
    return moves

def alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves=None):
    # put the white piece on the top then use put on bottom after
    print(whiteNum, otherNum, whiteLocation, otherLoc)
    if moves == None:
        moves = []
    cube = moveCube.getListCube()
    f, r, c = otherLoc
    for color in colors:
        if cube[f][r][c] in colors[color]:
            otherC = color
            break
    if whiteLocation[0] == 0:
        print("000000000")
        # base case is if white is on top
        i = 0
        print("locations", whiteLocation, otherLoc)
        while otherLoc[0] != colorToFace[otherC] and i < 4:
            i += 1
            moves.extend(makeMoves(moveCube, ["U"]))
            print("0 moves", i)
            l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
            print(l)
            whiteLocation, otherLoc = l
        return moves
    elif whiteLocation[0] == 2:
        print("2222222222")
        # move to top. Then goes to base case
        while whiteLocation[0] != 0:
            if otherLoc[0] == 0:
                moves.extend(makeMoves(moveCube, ["F", "R", "U'", "R'"]))
            elif otherLoc[0] == 1:
                moves.extend(makeMoves(moveCube, ["L'", "U'", "L"]))
            elif otherLoc[0] == 3:
                moves.extend(makeMoves(moveCube, ["R", "U", "R'"]))
            elif otherLoc[0] == 5:
                moves.extend(makeMoves(moveCube, ["F'", "R", "U'", "R'"]))
            # rotate cube back to normal position if it was rotated
            c = moveCube.getListCube()
            green = c[2][1][1]
            while green != 22:
                # green center piece is number 22 and is stationary relative to
                # the other centers
                moves.extend(makeMoves(moveCube, ["y"]))
                c = moveCube.getListCube()
                green = c[2][1][1]
            print("moves 2...", moves)
            l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
            whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)
    elif whiteLocation[0] == 5:
        print("5555555555")
        # move to top
        moves.extend(makeMoves(moveCube, moveCube.turnFace(f) * 2))
        l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
        whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)
    else:
        # recursive step
        # rotate the cube so that whiteLocation is 2
        print("white is...", whiteLocation)
        while whiteLocation[0] != 2:
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
            whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)

def putOnBottom(moveCube, edge, location, colors):
    moves = []
    white, otherColor = edge
    whiteLocation = location[0]
    otherLoc = location[1]
    moves.extend(alignEdge(moveCube, white, otherColor, whiteLocation, otherLoc, colors))
    # update locations
    whiteLocation, otherLoc = getLocation({white, otherColor}, moveCube, edges, corners)
    print("bottom put align", moves)
    print("white and other locations...", whiteLocation, otherLoc)
    # move particular edge to the bottom
    if otherLoc[0] == 1:
        moves.extend(makeMoves(moveCube, ["L2"]))
    elif otherLoc[0] == 2:
        moves.extend(makeMoves(moveCube, ["F2"]))
    elif otherLoc[0] == 3:
        moves.extend(makeMoves(moveCube, ["R2"]))
    elif otherLoc[0] == 4:
        moves.extend(makeMoves(moveCube, ["B2"]))
    print("move to bottom...", moves)
    # moves.extend(solveTheCross(moveCube, moveList))
    return moves







