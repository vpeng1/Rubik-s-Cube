# import all functions from rubikMoves and from scrambler

from rubikMoves import *
from scrambler import *

"""contains all the steps and algorithms used to solve a Rubik's Cube"""


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
################################################################################

# def rotateToStandard(moveCube, moves=None):
#     if moves == None:
#         moves = []
#     green = 22
#     yellow = 4
#     if moveCube.cube[3][1][1] == green or moveCube.cube[1][1][1] == green:
#         while moveCube.cube[0][1][1] != yellow:
#             moves.extend(makeMoves(moveCube, ["x"]))
#         while moveCube.cube[2][1][1] != green:
#             moves.extend(makeMoves(moveCube, ["y'"]))
#     elif moveCube.cube[2][1][1] == green or moveCube.cube[4][1][1] == green:
#         moves.extend(makeMoves(moveCube, ["y"]))
#         return rotateToStandard(moveCube, moves)
#     elif moveCube.cube[0][1][1] == green or moveCube.cube[5][1][1] == green:
#         moves.extend(makeMoves(moveCube, ["x"]))
#         return rotateToStandard(moveCube, moves)
#     return moves

def getColorEdges(colors, color):
    # returns a list of the edges with color color in the solved state
    # edges never change
    edges = [{7,19}, {14,21}, {23,30}, {25,46}, {5,28}, {3,10}, {1,37}, {32,39},
             {34,50}, {43,52}, {41,12}, {16,48}]
    c = colors[color]
    edgeList = []
    for edge in edges:
        if len(edge & c) != 0:
            edgeList.append(list(edge))
    return edgeList

def getLocation(piece, cube, ran = range(45, 54)):
    # use Moves.getListCube() to turn cube into a list
    # returns a list of the locations of the pieces in the current cube
    if not isinstance(cube, list):
        cube = cube.getListCube()
    edges = [{7, 19}, {14, 21}, {23, 30}, {25, 46}, {5, 28}, {3, 10}, {1, 37},
             {32, 39},
             {34, 50}, {43, 52}, {41, 12}, {16, 48}]
    corners = [{6, 11, 18}, {8, 20, 27}, {17, 24, 45}, {26, 33, 47},
               {2, 29, 36}, {35, 42, 53},
               {15, 44, 51}, {0, 9, 38}]
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
    assert(getLocation({52, 43}, cube) == [[2,1,2],[3,1,0]])
    print("Passed!")
testGetLocations()


# def edgeLocations(colorEdges, cube, edges, corners):
#     # returns the locations of all the edges of one color
#     # use getColorEdges
#     edgeLoc = []
#     for edge in colorEdges:
#         edgeLoc.append(getLocation(edge, cube, edges, corners))
#     return edgeLoc

whiteEdges = getColorEdges(colors, "white")
def solveCross(moveCube, whiteEdges, colors):
    # solves the white cross
    print("Solving Cross...", end="")
    moves = []
    for edge in whiteEdges:
        if correctEdgeLoc(edge, moveCube):
            continue
        cube = moveCube.getListCube()
        white, otherColor = edge
        location = getLocation({white, otherColor}, cube)
        moves.extend(putOnBottom(moveCube, [white, otherColor], location, colors))
        # print("solve", moves)
        cube = moveCube.getListCube()
    assert(cube[5][0][1] == 46)
    assert(cube[5][1][0] == 48)
    assert(cube[5][1][2] == 50)
    assert(cube[5][2][1] == 52)
    print("PASSED!!!!!!!!!!")
    return moves

def correctEdgeLoc(edge, moveCube):
    cube = moveCube.cube
    if edge == {25, 46}:
        return cube[5][0][1] == 46
    elif edge == {34, 50}:
        return cube[5][1][2] == 50
    elif edge == {43, 52}:
        return cube[5][2][1] == 52
    elif edge == {16, 48}:
        return cube[5][1][0]

def alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves=None):
    # aligns the edge on the upper face
    if moves == None:
        moves = []
    cube = moveCube.getListCube()
    f, r, c = otherLoc
    for color in colors:
        if cube[f][r][c] in colors[color]:
            otherC = color
            break
    if whiteLocation[0] == 0:
        # base case is if white is on top
        while otherLoc[0] != colorToFace[otherC]:
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation({whiteNum, otherNum}, moveCube)
            whiteLocation, otherLoc = l
        return moves
    elif whiteLocation[0] == 2:
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
            greenCenter = 22
            while green != greenCenter:
                # green center piece is number 22 and is stationary relative to
                # the other centers. Original location is face 2, row 1, col 1
                moves.extend(makeMoves(moveCube, ["y"]))
                green = moveCube.cube[2][1][1]
            l = getLocation({whiteNum, otherNum}, moveCube)
            whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)
    elif whiteLocation[0] == 5:
        # move to top
        moves.extend(makeMoves(moveCube, moveCube.turnFace(f) * 2))
        l = getLocation({whiteNum, otherNum}, moveCube)
        whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)
    else:
        # recursive step
        # rotate the cube so that whiteLocation[0] is 2
        # then go to base case
        while whiteLocation[0] != 2:
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation({whiteNum, otherNum}, moveCube)
            whiteLocation, otherLoc = l
        return alignEdge(moveCube, whiteNum, otherNum, whiteLocation, otherLoc, colors, moves)

def putOnBottom(moveCube, edge, location, colors):
    moves = []
    white, otherColor = edge
    whiteLocation = location[0]
    otherLoc = location[1]
    moves.extend(alignEdge(moveCube, white, otherColor, whiteLocation, otherLoc, colors))
    # update locations
    whiteLocation, otherLoc = getLocation({white, otherColor}, moveCube)
    # move particular edge to the bottom
    if otherLoc[0] == 1:
        moves.extend(makeMoves(moveCube, ["L2"]))
    elif otherLoc[0] == 2:
        moves.extend(makeMoves(moveCube, ["F2"]))
    elif otherLoc[0] == 3:
        moves.extend(makeMoves(moveCube, ["R2"]))
    elif otherLoc[0] == 4:
        moves.extend(makeMoves(moveCube, ["B2"]))
    return moves


################################################################################
#### Solving the White Corners ####
################################################################################

def getColorCorners(colors, color):
    # returns a list of corners that have the specified color
    cornerList = []
    corners = [{6, 11, 18}, {8, 20, 27}, {17, 24, 45}, {26, 33, 47},
               {2, 29, 36}, {35, 42, 53}, {15,44,51}, {0,9,38}]
    c = colors[color]
    for corner in corners:
        if len(corner & c) != 0:
            cornerList.append(corner)
    return cornerList


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
            newLocation.append(location[2])
    return newLocation

def getCorrectCorner(piece, colors):
    # returns the correct order of the colors on the corner piece
    cornerOrdering = [["white", "red", "green"], ["white", "blue", "red"],
                ["white", "orange", "blue"], ["white", "green", "orange"],
                ["yellow", "red", "blue"], ["yellow", "green", "red"],
                ["yellow", "orange", "green"], ["yellow", "blue", "orange"]]
    colorsSet = set()
    for color in colors:
        for num in piece:
            if num in colors[color]:
                colorsSet.add(color)
    for corn in cornerOrdering:
        if colorsSet == set(corn):
            return corn

whiteCorners = getColorCorners(colors, "white")
def solveCorners(moveCube, whiteCorners, colors):
    # solves the white corners
    print("Solving corners...", end="")
    moves = []
    cube = moveCube.getListCube()
    for corner in whiteCorners:
        if rightCornerLoc(corner, moveCube):
            continue
        else:
            location = getLocation(corner, cube)
            moves.extend(cornToBottom(moveCube, corner, location, colors))
            cube = moveCube.getListCube()
    assert(cube[5][0][0] == 45)
    assert(cube[5][0][2] == 47)
    assert(cube[5][2][0] == 51)
    assert(cube[5][2][2] == 53)
    print("Solved")
    return moves

def rightCornerLoc(corner, moveCube):
    cube = moveCube.cube
    print("corner", corner)
    if corner == {35, 42, 53}:
        return cube[5][2][2] == 53
    elif corner == {15, 44, 51}:
        return cube[5][2][0] == 51
    elif corner == {17, 24, 45}:
        return cube[5][0][0] == 45
    elif corner == {26, 33, 47}:
        return cube[5][0][2] == 47

def cornToBottom(moveCube, corner, location, colors):
    moves = []
    corn = getCorrectCorner(corner, colors)
    moves.extend(getCornTop(moveCube, location))
    loc = getLocation(corner, moveCube)
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
        if downSide[1] == 0:
            if downSide[2] == 0:
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
            l = getLocation(corner, moveCube)
            whiteLoc, loc1, loc2 = l
        while whiteLoc != [0, 2, 2]:
            # want the piece to be the bottom left piece on the upper face
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation(corner, moveCube)
            whiteLoc, loc1, loc2 = l
        moves.extend(makeMoves(moveCube, ["R", "U", "R'", "U'", "R", "U", "R'",
                                          "U'", "R", "U", "R'"]))
    elif loc1[0] == 0:
        # second color is on top. white side is to the left of the color
        while whiteLoc[0] != f1:
            # get white side to be on the face with the second color
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation(corner, moveCube)
            whiteLoc, loc1, loc2 = l
        while whiteLoc[0] != 1:
            # rotate cube so that the white side of the corner is on the left face
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation(corner, moveCube)
            whiteLoc, loc1, loc2 = l
        moves.extend(makeMoves(moveCube, ["L'", "U'", "L"]))
    elif loc2[0] == 0:
        # third side is on top. white side is to the right of that color
        while whiteLoc[0] != f2:
            moves.extend(makeMoves(moveCube, ["U"]))
            l = getLocation(corner, moveCube)
            whiteLoc, loc1, loc2 = l
        while whiteLoc[0] != 3:
            # rotate cube so that the white side is on the right face
            moves.extend(makeMoves(moveCube, ["y"]))
            l = getLocation(corner, moveCube)
            whiteLoc, loc1, loc2 = l
        moves.extend(makeMoves(moveCube, ["R", "U", "R'"]))
    green = moveCube.cube[2][1][1]
    greenCenter = 22
    while green != greenCenter:
        # green center piece is 22
        moves.extend(makeMoves(moveCube, ["y"]))
        green = moveCube.cube[2][1][1]
    return moves

################################################################################
#### Solve Second Layer ####
################################################################################

def getSetColorEdges(colors, color):
    # returns a list of the edge sets with color color in the solved state
    edges = [{7, 19}, {14, 21}, {23, 30}, {25, 46}, {5, 28}, {3, 10}, {1, 37},
             {32, 39}, {34,50}, {43,52}, {41,12}, {16,48}]
    c = colors[color]
    edgeList = []
    for edge in edges:
        if len(edge & c) != 0:
            edgeList.append(edge)
    return edgeList

def solveSecondLayer(moveCube, colors):
    print("Solving Second Layer...", end="")
    moves = []
    edges = layer2Edges(colors)
    for edge in edges:
        if right2EdgeLoc(edge, moveCube):
            continue
        moves.extend(align2Edge(moveCube, edge))
    try:
        cube = moveCube.cube
        assert (cube[2][1][0] == 21 and cube[1][1][2] == 14)
        assert (cube[2][1][2] == 23 and cube[3][1][0] == 30)
        assert (cube[3][1][2] == 32 and cube[4][1][0] == 39)
        assert (cube[4][1][2] == 41 and cube[1][1][0] == 12)
        print("Solved!")
    except:
        print("FAIL :(")
    return moves

def right2EdgeLoc(edge, moveCube):
    cube = moveCube.cube
    if edge == {21, 14}:
        return cube[2][1][0] == 21
    elif edge == {23, 30}:
        return cube[2][1][2] == 23
    elif edge == {32, 39}:
        return cube[3][1][2] == 32
    elif edge == {41, 12}:
        return cube[4][1][2] == 41

def layer2Edges(colors):
    # find the edges that do not have yellow or white in them
    edges = [{7, 19}, {14, 21}, {23, 30}, {25, 46}, {5, 28}, {3, 10}, {1, 37},
             {32, 39}, {34,50}, {43,52}, {41,12}, {16,48}]
    yellowEdges = getSetColorEdges(colors, "yellow")
    whiteEdges = getSetColorEdges(colors, "white")
    nonYellowWhite = []
    for edge in edges:
        if edge not in yellowEdges and edge not in whiteEdges:
            nonYellowWhite.append(edge)
    return nonYellowWhite

def align2Edge(moveCube, edge, moves=None):
    if moves == None:
        moves = []
    c1, c2 = getLocation(edge, moveCube)
    face1, face2 = getColors(c1, moveCube), getColors(c2, moveCube)
    if c1[0] == 0 or c2[0] == 0:
        # base case: edge piece is on the top layer
        while c1[0] != face1 and c2[0] != face2:
            # move edge on top to the correct face
            moves.extend(makeMoves(moveCube, ["U"]))
            c1, c2 = getLocation(edge, moveCube)
        while c1[0] != 2 and c2[0] != 2:
            # rotate so that it is on the front face
            moves.extend(makeMoves(moveCube, ["y"]))
            c1, c2 = getLocation(edge, moveCube)
        leftColor = getColors([1, 1, 1], moveCube)
        if leftColor == face1 or leftColor == face2:
            # sticker on top is the same color as the center sticker on the
            # face to the left
            moves.extend(makeMoves(moveCube,
                            ["U'", "L'", "U", "L", "U", "F", "U'", "F'"]))
        else:
            moves.extend(makeMoves(moveCube,
                            ["U", "R", "U'", "R'", "U'", "F'", "U", "F"]))
        green = moveCube.cube[2][1][1]
        while green != 22:
            moves.extend(makeMoves(moveCube, ["y"]))
            green = moveCube.cube[2][1][1]
    elif c1[0] == face1 and c2[0] == face2:
        # edge is already in the right place
        return moves
    else:
        # recursive step: edge piece is in the second layer
        while c1[0] != 2:
            # get the first side of the edge to be on the front face
            moves.extend(makeMoves(moveCube, ["y"]))
            c1, c2 = getLocation(edge, moveCube)
        if c1[2] == 0:
            # column is 0
            moves.extend(makeMoves(moveCube,
                                   ["U'", "L'", "U", "L", "U", "F", "U'", "F'"]))
        else:
            # column is 2
            moves.extend(makeMoves(moveCube,
                                   ["U", "R", "U'", "R'", "U'", "F'", "U", "F"]))
        green = moveCube.cube[2][1][1]
        greenCenter = 22
        while green != greenCenter:
            # rotate cube back to normal position
            moves.extend(makeMoves(moveCube, ["y"]))
            green = moveCube.cube[2][1][1]
        return align2Edge(moveCube, edge, moves)

    return moves

def getColors(location, moveCube):
    # returns the face for the color of the sticker at the particular location
    # green face has to be on the front for this to work
    colors = {"yellow": set(range(9)), "red": set(range(9, 18)), "green":
        set(range(18, 27)), "orange": set(range(27, 36)), "blue":
                  set(range(36, 45)), "white": set(range(45, 54))}
    colorToFace = {"yellow": 0, "red": 1, "green": 2, "orange": 3, "blue": 4,
                   "white": 5}
    f, r, c = location
    for color in colors:
        if moveCube.cube[f][r][c] in colors[color]:
            return colorToFace[color]

################################################################################
#### Solve Yellow Cross ####
################################################################################

def remainingEdges(colors):
    return getSetColorEdges(colors, "yellow")

def solveYellowCross(moveCube, moves=None):
    if moves == None:
        moves = []
    numOnTop = 0
    # numOnTop counts the number of edges in which the yellow side is on the top
    yellowEdges = remainingEdges(colors)
    for edge in yellowEdges:
        yellow, other = getLocation(edge, moveCube, range(9))
        if yellow[0] == 0:
            numOnTop += 1
    if numOnTop == 4:
        # all edges have yellow facing up
        return moves
    elif numOnTop == 0:
        # recursive step: none of the edges have yellow facing up
        moves.extend(makeMoves(moveCube, ["F", "R", "U", "R'", "U'", "F'"]))
        return solveYellowCross(moveCube, moves)
    else:
        cube = moveCube.getListCube()
        if cube[0][1][0] in range(9) and cube[0][1][2] in range(9):
            # yellow pieces form a horizontal line with the center piece
            moves.extend(makeMoves(moveCube, ["F", "R", "U", "R'", "U'", "F'"]))
            return moves
        elif cube[0][0][1] in range(9) and cube[0][2][1] in range(9):
            # form a vertical line
            moves.extend(makeMoves(moveCube, ["U", "F", "R", "U", "R'", "U'", "F'"]))
            return moves
        else:
            while cube[0][0][1] not in range(9) or cube[0][1][0] not in range(9):
                # need top edge and left edge to be yellow
                moves.extend(makeMoves(moveCube, ["U"]))
                cube = moveCube.getListCube()
            moves.extend(makeMoves(moveCube,
                    ["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"]))
            return moves

def permuteYellowEdges(moveCube):
    cube = moveCube.getListCube()
    moves = []
    if (cube[1][0][1] == 10) and (cube[2][0][1] == 19) and \
            (cube[3][0][1] == 28) and (cube[4][0][1] == 37):
        return moves
    i = 0
    while (cube[1][0][1] not in range(9, 18) or cube[2][0][1] not in
            range(18, 27)) and (cube[2][0][1] not in range(18, 27) or
            cube[3][0][1] not in range(27, 36)) and (cube[3][0][1] not in
            range(27, 36) or cube[4][0][1] not in range(36, 45)) and \
            (cube[4][0][1] not in range(36, 45) or cube[1][0][1] not in
            range(9, 18)):
        # want two adjacent edges to be in the correct position relative to each
        # other
        moves.extend(makeMoves(moveCube, ["U"]))
        if (cube[1][0][1] == 10) and (cube[2][0][1] == 19) and \
                (cube[3][0][1] == 28) and (cube[4][0][1] == 37):
            return moves
        i += 1
        if i == 4:
            # case in which no two adjacent edges are in the correct
            # positions relative to each other
            moves.extend(makeMoves(moveCube,
                                   ["R", "U", "R'", "U", "R", "U2", "R'", "U"]))
        cube = moveCube.getListCube()

    while getColors([3, 0, 1], moveCube) != getColors([3, 1, 1], moveCube) \
            or getColors([4, 0, 1], moveCube) != getColors([4, 1, 1], moveCube):
        # need the edges on the third face and the fourth face to be permuted
        # correctly
        moves.extend(makeMoves(moveCube, ["y"]))
    moves.extend(makeMoves(moveCube, ["R", "U", "R'", "U", "R", "U2", "R'", "U"]))
    green = moveCube.cube[2][1][1]
    greenCenter = 22
    while green != greenCenter:
        moves.extend(makeMoves(moveCube, ["y"]))
        green = moveCube.cube[2][1][1]
    return moves

def inRightLocation(corner, moveCube, colors):
    # checks if a corner is in the correct location
    yellow, loc1, loc2 = getLocation(corner, moveCube, range(9))
    yel, c1, c2 = getCorrectCorner(corner, colors)
    if yellow[0] == 0:
        # yellow side of the corner is in the top face
        if colorToFace[c1] == loc1[0] and colorToFace[c2] == loc2[0]:
            # piece is on the correct face
            return True
    elif loc1[0] == 0:
        # color clockwise to the yellow face is in the top face
        if moveCube.cube[loc2[0]][loc2[1]][1] in colors[c1] and \
                moveCube.cube[yellow[0]][yellow[1]][1] in colors[c2]:
            return True
    elif loc2[0] == 0:
        # color ccw to the yellow face is in the top face
        if moveCube.cube[loc1[0]][loc1[1]][1] in colors[c2] and \
                moveCube.cube[yellow[0]][yellow[1]][1] in colors[c1]:
            return True
    return False

def rightLocation(loc, moveCube, colors):
    left, top, right = loc
    x = [[3, 0, 2], [0, 0, 2], [4, 0, 0]]
    cube = moveCube.getListCube()
    for color in colors:
        if cube[3][0][2] in colors[color] and cube[3][0][1] in colors[color]:
            # permuted and oriented correctly
            return True
        elif cube[3][0][2] in colors[color] and cube[4][0][1] in colors[color] \
                and cube[4][0][0] in range(9):
            # left has the color of the right face and right has the
            # color of the top face
            return True
        elif cube[0][0][2] in colors[color] and cube[4][0][1] in colors[color] \
                and cube[3][0][2] in range(9):
            return True
    return False


yellowCorners = getColorCorners(colors, "yellow")
def permuteYellowCorners(moveCube, yellowCorners, colors, colorToFace, moves=None, depth=0):
    if moves == None:
        moves = []
    for i in range(len(yellowCorners)):
        if inRightLocation(yellowCorners[i], moveCube, colors):
            if inRightLocation(yellowCorners[(i+1)%4], moveCube, colors):
                # if at least 2 corners are permuted correctly then all corners
                # are permuted correctly
                return moves
            while moveCube.cube[2][0][2] not in yellowCorners[i]:
                moves.extend(makeMoves(moveCube, ["y"]))
            moves.extend(makeMoves(moveCube, ["U", "R", "U'", "L'", "U", "R'",
                                              "U'", "L"]))

            if not inRightLocation(yellowCorners[(i+1)%4], moveCube, colors):
                # inverse rotation requires doing the algorithm twice
                print("what is wrong with this")
                moves.extend(makeMoves(moveCube, ["U", "R", "U'", "L'", "U",
                                                  "R'", "U'", "L"]))
            while moveCube.cube[2][1][1] != 22:
                moves.extend(makeMoves(moveCube, ["y"]))
            return moves
    # if not permuted correctly, repeat this step
    moves.extend(makeMoves(moveCube,
                           ["U", "R", "U'", "L'", "U", "R'", "U'", "L"]))
    return permuteYellowCorners(moveCube, yellowCorners, colors, colorToFace, moves)

def orientYellowCorners(moveCube, yellowCorners):
    moves = []
    for corner in yellowCorners:
        yellow, loc1, loc2 = getLocation(corner, moveCube, range(9))
        if yellow[0] != 0:
            topRight = [[2, 0, 1], [0, 2, 2], [3, 0, 0]]
            while yellow not in topRight and loc1 not in topRight and \
                    loc2 not in topRight:
                # want the corner piece to be on the top right
                moves.extend(makeMoves(moveCube, ["U"]))
                yellow, loc1, loc2 = getLocation(corner, moveCube, range(9))
            while yellow[0] != 0:
                moves.extend(makeMoves(moveCube, ["R'", "D'", "R", "D"]))
                yellow, loc1, loc2 = getLocation(corner, moveCube, range(9))

    greenFrontEdge = 19
    while moveCube.cube[2][0][1] != greenFrontEdge:
        # adjust upper face
        moves.extend(makeMoves(moveCube, ["U"]))
    return moves

def solveLastLayer(moveCube, moves=None):
    if moves == None:
        moves = []
    print("Solving Yellow Cross...", end="")
    moves.extend(solveYellowCross(moveCube))
    cube = moveCube.getListCube()
    assert(cube[0][0][1] in range(9))
    assert(cube[0][1][0] in range(9))
    assert(cube[0][1][2] in range(9))
    assert(cube[0][2][1] in range(9 ))
    print("Cross Solved!!!")

    print("Permuting Yellow Edges...", end="")
    moves.extend(permuteYellowEdges(moveCube))
    assert(cube[1][0][1] == 10)
    assert(cube[2][0][1] == 19)
    assert(cube[3][0][1] == 28)
    assert(cube[4][0][1] == 37)
    print("Permuted!!!")
    moves.extend(tryPermuteOrientCorners(moveCube, yellowCorners, colors, colorToFace))
    if moveCube.cube != solved:
        return solveLastLayer(moveCube, moves)
    print("last layer: ", moves)
    print("CUBE IS SOLVED!!!")
    return moves

def tryPermuteOrientCorners(moveCube, yellowCorners, colors, colorToFace, moves=None, depth=0):
    if moves == None:
        moves = []
    cube = moveCube.getListCube()
    perm = permuteYellowCorners(moveCube, yellowCorners, colors, colorToFace)
    moves.extend(perm)
    # print("last layer moves:", moves)
    print("Permuting Yellow Corners...", end="")
    assert (cube[1][0][1] == 10)
    assert (cube[2][0][1] == 19)
    assert (cube[3][0][1] == 28)
    assert (cube[4][0][1] == 37)
    print("Permuted!!!")
    print("Orienting Yellow Corners...")
    orient = orientYellowCorners(moveCube, yellowCorners)
    moves.extend(orient)
    try:
        cube = moveCube.getListCube()
        assert (cube[0] == solved[0])
        assert (cube[1] == solved[1])
        assert (cube[2] == solved[2])
        assert (cube[3] == solved[3])
        assert (cube[4] == solved[4])
        assert (cube[5] == solved[5])
        assert (cube == solved)
        print("Oriented!")
        return moves
    except:
        r = reverseAlg(orient)
        p = reverseAlg(perm)
        moves.extend(makeMoves(moveCube, r))
        moves.extend(makeMoves(moveCube, p))
        moves.extend(makeMoves(moveCube, ["U", "R", "U'", "L'", "U",
                                          "R'", "U'", "L"]))
        if depth == 1:
            moves.extend(makeMoves(moveCube, ["R", "U", "R'", "U", "R", "U2", "R'"]))
            return moves

        # case in which the corners were not permuted properly in the
        # permutation step
        return tryPermuteOrientCorners(moveCube, yellowCorners, colors,
                                       colorToFace, moves, depth+1)


