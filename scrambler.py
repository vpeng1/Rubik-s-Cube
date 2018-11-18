
from rubikMoves import *
import random

def scrambleAlgorithm():
    # returns a scramble algorithm for the cube
    numMoves = 25
    moveList = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'",
                "D2", "F", "F'", "F2", "B", "B'", "B2"]
    scramble = []
    prevMove = "0"
    while len(scramble) < numMoves:
        move = random.choice(moveList)
        if move[0] != prevMove[0]:
            # to prevent making the same move twice in a row
            scramble.append(move)
        prevMove = move
    return scramble

def reverseScramble(scramble):
    # reverses the scramble
    rScramble = []
    for i in range(len(scramble)-1, -1, -1):
        if "2" in scramble[i]:
            rScramble.append(scramble[i])
        elif "'" in scramble[i]:
            rScramble.append(scramble[i][0])
        elif "'" not in scramble[i]:
            rScramble.append(scramble[i] + "'")
    return rScramble

def scrambleCube(scramble):
    # returns the scrambled cube
    solvedU = \
        [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    solvedL = \
        [[9, 10, 11],
         [12, 13, 14],
         [15, 16, 17]]
    solvedF = \
        [[18, 19, 20],
         [21, 22, 23],
         [24, 25, 26]]
    solvedR = \
        [[27, 28, 29],
         [30, 31, 32],
         [33, 34, 35]]
    solvedB = \
        [[36, 37, 38],
         [39, 40, 41],
         [42, 43, 44]]
    solvedD = \
        [[45, 46, 47],
         [48, 49, 50],
         [51, 52, 53]]
    cube = [solvedU, solvedL, solvedF, solvedR, solvedB, solvedD]
    solved = Cube(cube)
    assert(type(solved) == Cube)
    return makeMoves(solved, scramble)

def testScramble():
    print("Testing scrambler...", end="")
    s = scrambleAlgorithm()
    c = scrambleCube(s)
    r = reverseScramble(s)
    solution = makeMoves(c, r)
    assert(str(solution) == str(solved))
    assert(isinstance(c, Cube))
    cube = c.getListCube()
    assert(isinstance(cube, list))
    print("Passed!")

testScramble()

