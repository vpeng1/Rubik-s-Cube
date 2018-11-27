from scrambler import *
from rubikMoves import *
from algorithms import *
import time

#### append each algorithm to a list of moves

def reduceMoves(moves):
    # takes in a list of moves and gets rid of unnecessary moves
    # returns a simplified list of moves
    prevMove = "0"
    i = 0
    while i < len(moves):
        if moves[i][0] == prevMove[0]:
            if len(moves[i]) == 1 and len(prevMove) == 2:
                # prev is either a prime move or a 2 move
                if prevMove[1] == "'":
                    moves.pop(i - 1)
                    moves.pop(i - 1)
                    if i >= 2:
                        prevMove = moves[i - 2]
                    else:
                        prevMove = "0"
                    i -= 1
                elif prevMove[1] == "2":
                    moves[i-1] = moves[i] + "'"
                    moves.pop(i)
                    if i >= 1:
                        prevMove = moves[i - 1]
                    else:
                        prevMove = "0"

            elif len(moves[i]) == 2 and len(prevMove) == 1:
                # move[i] is either a prime move or a 2 move
                if moves[i][1] == "'":
                    moves.pop(i - 1)
                    moves.pop(i - 1)
                    if i >= 2:
                        prevMove = moves[i - 2]
                    else:
                        prevMove = "0"
                    i -= 1
                elif moves[i][1] == "2":
                    moves[i-1] = moves[i] + "'"
                    moves.pop(i)
                    if i >= 1:
                        prevMove = moves[i - 1]
                    else:
                        prevMove = "0"

            elif len(moves[i]) == len(prevMove) == 2:
                # both are primes or both are 2s or one of each
                if "2" in moves[i] and "2" in prevMove:
                    moves.pop(i-1)
                    moves.pop(i-1)
                    if i >= 2:
                        prevMove = moves[i - 2]
                    else:
                        prevMove = "0"
                    i -= 1

                elif "2" in moves[i] and "2" not in prevMove:
                    moves[i-1] = prevMove[0]
                    moves.pop(i)
                    if i >= 1:
                        prevMove = moves[i - 1]
                    else:
                        prevMove = "0"

                elif "2" not in moves[i] and "2" in prevMove:
                    moves[i-1] = prevMove[0]
                    moves.pop(i)
                    if i >= 1:
                        prevMove = moves[i - 1]
                    else:
                        prevMove = "0"

                elif "2" not in moves[i] and "2" not in prevMove:
                    moves[i-1] = prevMove[0] + "2"
                    moves.pop(i)
                    if i >= 1:
                        prevMove = moves[i - 1]
                    else:
                        prevMove = "0"

            elif moves[i] == prevMove:
                moves[i-1] = moves[i][0] + "2"
                moves.pop(i)
                if i >= 1:
                    prevMove = moves[i - 1]
                else:
                    prevMove = "0"

        else:
            prevMove = moves[i]
            i += 1
    if not isReduced(moves):
        return reduceMoves(moves)
    return moves

def isReduced(moves):
    for i in range(len(moves) - 1):
        if moves[i][0] == moves[i+1][0]:
            return False
    return True

def testReduceMoves():
    print("Testing Reduce Moves...", end="")
    assert(reduceMoves(["R", "R", "R", "R","U2", "U2", "U'"]) == ["U'"])
    assert(reduceMoves(["R", "L", "U", "U'", "U", "L2", "L2", "B"]) ==
           ["R", "L", "U", "B"])
    print("Passed!")

testReduceMoves()
solvedU = \
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
solvedL = \
    [[9, 10, 11],
     [12, 13,14],
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

solved = [solvedU, solvedL, solvedF, solvedR, solvedB, solvedD]

t0 = time.time()
s = scrambleAlgorithm()
print(s)
c = scrambleCube(s)
print("scramble", c)
def solveCube(c):
    if c.cube != solved:
        t1 = time.time()
        x = solveCross(c, whiteEdges, colors)
        x1 = reduceMoves(x)
        print(len(x1), x1)
        t2 = time.time()
        y = solveCorners(c, whiteCorners, colors)
        y1 = reduceMoves(y)
        print(len(y1), y1)
        t3 = time.time()
        z = solveSecondLayer(c, colors)
        z1 = reduceMoves(z)
        print(len(z1), z1)
        t4 = time.time()
        a = solveLastLayer(c)
        a1 = reduceMoves(a)
        print(len(a1), a1)
        t5 = time.time()
        reduced = reduceMoves(x1+y1+z1+a1)
        print(len(x1) + len(y1) + len(z1) + len(a1))
        print("Reduced Moves", len(reduced), reduced)
        return reduced

        print()
        # print("scramble time:", t1-t0)
        print("cross time:", t2-t1)
        print("corners time:", t3-t2)
        print("second layer time:", t4-t3)
        print("last layer time:", t5-t4)
        print("total time:", t5-t1)
    else:
        print("Cube is already solved!!!")
solveCube(c)



