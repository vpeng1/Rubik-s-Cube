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

t1 = time.time()
s = scrambleAlgorithm()
print(s)
c = scrambleCube(s)
print("c", c)
print("Solving Cross...")
x = solveCross(c, whiteEdges, colors)
# print("x", x)
print(reduceMoves(x))
t2 = time.time()
print(t2-t1)
t3 = time.time()
y = solveCorners(c, whiteCorners, colors)
# print("y", y)
print(reduceMoves(y))
t4 = time.time()
print(t4-t3)





