# import all functions from rubikMoves and from scrambler

from rubikMoves import *
from scrambler import *

"""contains all the steps to solve the cube"""

edges = [{7,19}, {14,21}, {23,30}, {25,46}, {5,28}, {3,10}, {1,37}, {32,39},
         {34,50}, {43,52}, {41,12}, {16,48}]
corners = [{6,11,18}, {8,20,27}, {17,24,45}, {26,33,47}, {2,29,36}, {35,42,53},
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

################################################################################
#### Solving the White Edges ####

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
                            return checkEdgeLocation(cube, location, ran)
                    elif piece in corners:
                        if len(location) == 3:
                            return checkCornerLocation(cube, piece, location, colors)


def checkEdgeLocation(cube, location, rangeValues):
    # in the case of solving the white cross, rangeValues would be range(45, 54)
    f, r, c = location[0]
    if cube[f][r][c] not in rangeValues:
        # want first index to be the index for the side in rangeValues
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
    assert(getLocation({52, 43}, cube, edges, corners) == [[2,1,2],[3,1,0]])
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
        # print("solving for edge", edge)
        cube = moveCube.getListCube()
        if edge[0] in colors["white"]:
            white = edge[0]
            otherColor = edge[1]
        else:
            white = edge[1]
            otherColor = edge[0]
        location = getLocation({white, otherColor}, cube, edges, corners)
        moves.extend(putOnBottom(moveCube, [white, otherColor], location, colors))
        # print("solve", moves)
        cube = moveCube.getListCube()
    assert(cube[5][0][1] == 46)
    assert(cube[5][1][0] == 48)
    assert(cube[5][1][2] == 50)
    assert(cube[5][2][1] == 52)
    print("PASSED!!!!!!!!!!")
    return moves

def alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves=None):
    # aligns the edge on the upper face
    # print(whiteNum, otherNum, whiteLocation, otherLoc)
    if moves == None:
        moves = []
    cube = moveCube.getListCube()
    f, r, c = otherLoc
    for color in colors:
        if cube[f][r][c] in colors[color]:
            otherC = color
            break
    if whiteLocation[0] == 0:
        # print("000000000")
        # base case is if white is on top
        # i = 0
        # print("locations", whiteLocation, otherLoc)
        while otherLoc[0] != colorToFace[otherC]: # and i < 4:
            # i += 1
            moves.extend(makeMoves(moveCube, ["U"]))
            # print("0 moves", i)
            l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
            # print(l)
            whiteLocation, otherLoc = l
        return moves
    elif whiteLocation[0] == 2:
        # print("2222222222")
        # move to top. Then go to base case
        while whiteLocation[0] != 0:
            if otherLoc[0] == 0:
                moves.extend(makeMoves(moveCube, ["F", "R", "U'", "R'", "F'"]))
            elif otherLoc[0] == 1:
                moves.extend(makeMoves(moveCube, ["L'", "U'", "L"]))
            elif otherLoc[0] == 3:
                moves.extend(makeMoves(moveCube, ["R", "U", "R'"]))
            elif otherLoc[0] == 5:
                moves.extend(makeMoves(moveCube, ["F'", "R", "U'", "R'"]))
            # rotate cube back to normal position if it was rotated
            c = moveCube.getListCube()
            green = moveCube.cube[2][1][1]
            while green != 22:
                # green center piece is number 22 and is stationary relative to
                # the other centers. Original location is face 2, row 1, col 1
                moves.extend(makeMoves(moveCube, ["y"]))
                green = moveCube.cube[2][1][1]
            # print("moves 2...", moves)
            l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
            whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)
    elif whiteLocation[0] == 5:
        # print("5555555555")
        # move to top
        moves.extend(makeMoves(moveCube, moveCube.turnFace(f) * 2))
        l = getLocation({whiteNum, otherNum}, moveCube, edges, corners)
        whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)
    else:
        # recursive step
        # rotate the cube so that whiteLocation is 2
        # then go to base case
        # print("white is...", whiteLocation)
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
    # print("bottom put align", moves)
    # print("white and other locations...", whiteLocation, otherLoc)
    # move particular edge to the bottom
    if otherLoc[0] == 1:
        moves.extend(makeMoves(moveCube, ["L2"]))
    elif otherLoc[0] == 2:
        moves.extend(makeMoves(moveCube, ["F2"]))
    elif otherLoc[0] == 3:
        moves.extend(makeMoves(moveCube, ["R2"]))
    elif otherLoc[0] == 4:
        moves.extend(makeMoves(moveCube, ["B2"]))
    # print("move to bottom...", moves)
    # moves.extend(solveTheCross(moveCube, moveList))
    return moves


################################################################################
#### Solving the White Corners ####

def getColorCorners(corners, colors, color):
    # returns a list of corners that have the specified color
    cornerList = []
    c = colors[color]
    for corner in corners:
        if len(corner & c) != 0:
            cornerList.append(corner)
    return cornerList

# getLocation is in the algorithms.py file

def checkCornerLocation(cube, piece, location, colors):
    # want corners to be ordered with white first then the other colors
    # clockwise
    newLocation = []
    f, r, c = location[0]
    f1, r1, c1 = location[1]
    order = getCorrectCorner(piece, colors)
    for color in order:
        if cube[f][r][c] in colors[color]:
            newLocation.append(location[0])
        elif cube[f1][r1][c1] in colors[color]:
            newLocation.append(location[1])
        else:
            "WHY????!!!!???!?!?!"
            newLocation.append(location[2])
    return newLocation

def getCorrectCorner(piece, colors):
    cornerOrdering = [["white", "red", "green"], ["white", "blue", "red"],
                      ["white", "orange", "blue"], ["white", "green", "orange"]]
    colorsSet = set()
    for color in colors:
        for num in piece:
            if num in colors[color]:
                colorsSet.add(color)
    for corn in cornerOrdering:
        if colorsSet == set(corn):
            return corn

print(getCorrectCorner({17, 45, 24}, colors))

whiteCorners = getColorCorners(corners, colors, "white")
def solveCorners(moveCube, whiteCorners, colors):
    # solves the white corners
    moves = []
    cube = moveCube.getListCube()
    # print("whiteCorners", whiteCorners)
    for corner in whiteCorners:
        location = getLocation(corner, cube, edges, corners)
        # print("THis is the lcoation", location)
        moves.extend(cornToBottom(moveCube, corner, location, colors))
        # print("corner is...", corner)
        # print("corner moves", moves)

        cube = moveCube.getListCube()
    # print(moves)
    assert(cube[5][0][0] == 45)
    assert(cube[5][0][2] == 47)
    assert(cube[5][2][0] == 51)
    assert(cube[5][2][2] == 53)
    print("YES!!!")

    return moves

def cornToBottom(moveCube, corner, location, colors):
    moves = []
    corn = getCorrectCorner(corner, colors)
    moves.extend(getCornTop(moveCube, location))
    loc = getLocation(corner, moveCube, edges, corners)
    # print("bottom loc", loc)
    moves.extend(alignCorn(moveCube, corn, loc, corner, colorToFace))
    return moves

def getCornTop(moveCube, location):
    # moves the corner to the upper face if it is on the down face
    moves = []
    downSide = None
    for side in location:
        if side[0] == 5:
            downSide = side
    if downSide != None:
        # print("move to top", location)
        if downSide[1] == 0: # row 0
            if downSide[2] == 0: # col 0
                moves.extend(makeMoves(moveCube, ["F", "U", "F'"]))
            else:
                moves.extend(makeMoves(moveCube, ["F'", "U'", "F"]))
        elif downSide[1] == 2:
            if downSide[2] == 0:
                moves.extend(makeMoves(moveCube, ["B'", "U'", "B"]))
            else:
                moves.extend(makeMoves(moveCube, ["B", "U", "B'"]))
    return moves

def alignCorn(moveCube, corn, location, corner, colorToFace, moves=None):
    # places the corner above the location it needs to go in
    # corn is a list of the colors of the corners
    if moves == None:
        moves = []
    # print("align", location)
    whiteLoc, loc1, loc2 = location
    white, c1, c2 = corn
    f1 = colorToFace[c1]
    f2 = colorToFace[c2]
    if whiteLoc[0] == 0:
        # white is on top
        # move the piece above the location it should be in
        color2 = colorToFace[c2]
        while loc1[0] != color2:
            # c1 will be on the face with the c2 center
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation(corner, moveCube, edges, corners)
            # print("l is...", l, whiteLoc)
            whiteLoc, loc1, loc2 = l
        while whiteLoc != [0, 2, 2]:
            # want the piece to be the bottom left piece on the upper face
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation(corner, moveCube, edges, corners)
            # print("l is...", l, whiteLoc)
            whiteLoc, loc1, loc2 = l
        moves.extend(makeMoves(moveCube, ["R", "U", "R'", "U'", "R", "U", "R'",
                                          "U'", "R", "U", "R'"]))

    elif loc1[0] == 0:
        # second color is on top. white side is to the left of the color
        while whiteLoc[0] != f1:
            # get white side to be on the face with the second color
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation(corner, moveCube, edges, corners)
            # print("l is...", l, whiteLoc)
            whiteLoc, loc1, loc2 = l
        while whiteLoc[0] != 1:
            # rotate cube so that the white side of the corner is on the left face
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation(corner, moveCube, edges, corners)
            # print("l is...", l, whiteLoc)
            whiteLoc, loc1, loc2 = l
        moves.extend(makeMoves(moveCube, ["L'", "U'", "L"]))
    elif loc2[0] == 0:
        # third side is on top. white side is to the right of that color
        while whiteLoc[0] != f2:
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation(corner, moveCube, edges, corners)
            # print("l is...", l, whiteLoc)
            whiteLoc, loc1, loc2 = l
        while whiteLoc[0] != 3:
            # rotate cube so that the white side is on the right face
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation(corner, moveCube, edges, corners)
            # print("l is...", l, whiteLoc)
            whiteLoc, loc1, loc2 = l
        moves.extend(makeMoves(moveCube, ["R", "U", "R'"]))
    green = moveCube.cube[2][1][1]
    while green != 22:
        # green center piece is 22
        moves.extend(makeMoves(moveCube, ["y"]))
        green = moveCube.cube[2][1][1]
    return moves





