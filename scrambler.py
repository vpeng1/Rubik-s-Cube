# import from rubikMoves and import random

""" Contains functions that produce a randomly scrambled Rubik's Cube"""

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
            # to prevent rotating the same face twice in a row
            scramble.append(move)
        prevMove = move
    return scramble

def reverseAlg(alg):
    # reverses the algorithm
    rAlg = []
    for i in range(len(alg)-1, -1, -1):
        if "2" in alg[i]:
            rAlg.append(alg[i])
        elif "'" in alg[i]:
            rAlg.append(alg[i][0])
        elif "'" not in alg[i]:
            rAlg.append(alg[i] + "'")
    return rAlg

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
    c = Cube(cube)
    assert(type(c) == Cube)
    makeMoves(c, scramble)
    return c

def testScramble():
    print("Testing scrambler...", end="")
    s = scrambleAlgorithm()
    c = scrambleCube(s)
    r = reverseAlg(s)
    makeMoves(c, r)
    assert(str(c) == str(solved))
    assert(isinstance(c, Cube))
    cube = c.getListCube()
    assert(isinstance(cube, list))
    print("Passed!")

testScramble()

