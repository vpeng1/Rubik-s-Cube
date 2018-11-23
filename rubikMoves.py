
# visual representation of cube layout. Not used anywhere
solved1 = [
              [0,  1,  2 ],
              [3,  4,  5 ],
              [6,  7,  8 ],
[9, 10, 11],  [18, 19, 20], [27, 28, 29], [36, 37, 38],
[12, 13,14],  [21, 22, 23], [30, 31, 32], [39, 40, 41],
[15, 16, 17], [24, 25, 26], [33, 34, 35], [42, 43, 44],
              [45, 46, 47],
              [48, 49, 50],
              [51, 52, 53]
             ]




# actual representation of solved cube
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

import copy
class Cube(object):
    def __init__(self, cube):
        self.cube = cube
        self.c = copy.deepcopy(self.cube)
        self.upper = self.cube[0]
        self.left = self.cube[1]
        self.front = self.cube[2]
        self.right = self.cube[3]
        self.back = self.cube[4]
        self.down = self.cube[5]

    def turnRight(self):
        # turns the right face clockwise
        c = self.c
        r = copy.deepcopy(self.right)
        rightCol = 2
        for row in range(3):
            self.upper[row][rightCol] = c[2][row][rightCol]
            self.front[row][rightCol] = c[5][row][rightCol]
            self.down[row][rightCol] = c[4][2-row][0]
            self.back[row][0] = c[0][2-row][rightCol]
            for col in range(3):
                self.right[row][col] = r[2-col][row]
        self.c = copy.deepcopy(self.cube)
        return self.cube

    def turnLeft(self):
        c = self.c
        l = copy.deepcopy(self.left)
        leftCol = 0
        for row in range(3):
            self.upper[row][leftCol] = c[4][2-row][2]
            self.front[row][leftCol] = c[0][row][leftCol]
            self.down[row][leftCol] = c[2][row][leftCol]
            self.back[row][2] = c[5][2-row][leftCol]
            for col in range(3):
                self.left[row][col] = l[2-col][row]
        self.c = copy.deepcopy(self.cube)
        return self.cube

    def turnUp(self):
        c = self.c
        u = copy.deepcopy(self.upper)
        upRow = 0
        for col in range(3):
            self.left[upRow][col] = c[2][upRow][col]
            self.front[upRow][col] = c[3][upRow][col]
            self.right[upRow][col] = c[4][upRow][col]
            self.back[upRow][col] = c[1][upRow][col]
            for row in range(3):
                self.upper[row][col] = u[2-col][row]
        self.c = copy.deepcopy(self.cube)
        return self.cube

    def turnDown(self):
        c = self.c
        d = copy.deepcopy(self.down)
        downRow = 2
        for col in range(3):
            self.left[downRow][col] = c[4][downRow][col]
            self.front[downRow][col] = c[1][downRow][col]
            self.right[downRow][col] = c[2][downRow][col]
            self.back[downRow][col] = c[3][downRow][col]
            for row in range(3):
                self.down[row][col] = d[2-col][row]
        self.c = copy.deepcopy(self.cube)
        return self.cube

    def turnFront(self):
        f = copy.deepcopy(self.front)
        u = copy.copy(self.upper[2])
        r = [self.right[i][0] for i in range(3)]
        l = [self.left[i][2] for i in range(3)]
        d = copy.copy(self.down[0])
        for row in range(3):
            self.right[row][0] = u[row]
            self.down[0][row] = r[2 - row]
            self.left[row][2] = d[row]
            self.upper[2][row] = l[2 - row]
            for col in range(3):
                self.front[row][col] = f[2 - col][row]
        self.c = copy.deepcopy(self.cube)
        return self.cube

    def turnBack(self):
        b = copy.deepcopy(self.back)
        u = copy.copy(self.upper[0])
        l = [self.left[i][0] for i in range(3)]
        r = [self.right[i][2] for i in range(3)]
        d = copy.copy(self.down[2])
        for row in range(3):
            self.upper[0][row] = r[row]
            self.right[row][2] = d[2 - row]
            self.down[2][row] = l[row]
            self.left[row][0] = u[2 - row]
            for col in range(3):
                self.back[row][col] = b[2 - col][row]
        self.c = copy.deepcopy(self.cube)
        return self.cube

    def getListCube(self):
        # returns the cube in a 3d list
        return self.cube

    def turnFace(self, face):
        if face == 0:
            return ["U"]
        elif face == 1:
            return ["L"]
        elif face == 2:
            return ["F"]
        elif face == 3:
            return ["R"]
        elif face == 4:
            return ["B"]
        elif face == 5:
            return ["D"]

    def rotateYaxis(self):
        # rotates the cube around the y-axis clockwise relative to the down face
        d = copy.deepcopy(self.down)
        u = copy.deepcopy(self.upper)
        for row in range(3):
            self.left[row], self.front[row], self.right[row], self.back[row] = \
                self.back[row], self.left[row], self.front[row], self.right[row]
            for col in range(3):
                self.down[row][col] = d[2-col][row]
                self.upper[row][col] = u[col][2-row]
        self.c = copy.deepcopy(self.cube)
        return self.cube


    # def rotateRightFace(self):
    #     # 5, 9, 13 are the rows for the right face
    #     t0 = time.time()
    #     r1 = self.cube[5] + []
    #     r2 = self.cube[9] + []
    #     r3 = self.cube[13] + []
    #     self.cube[5][0] = r3[0]
    #     self.cube[5][1] = r2[0]
    #     self.cube[5][2] = r1[0]
    #     self.cube[9][0] = r3[1]
    #     self.cube[9][2] = r1[1]
    #     self.cube[13][0] = r3[2]
    #     self.cube[13][1] = r2[2]
    #     self.cube[13][2] = r1[2]
    #     t1 = time.time()
    #     print(t1-t0)
    #     return self.cube

    # def rotateRightFace(self):
    #     # 5, 9, 13 are the rows for the right face
    #     t0 = time.time()
    #     face = [self.cube[5], self.cube[9], self.cube[13]]
    #     f = [self.cube[5][:], self.cube[9][:], self.cube[13][:]]
    #     for row in range(3):
    #         for col in range(3):
    #             face[row][col] = f[2-col][row]
    #     t1 = time.time()
    #     print(t1-t0)
    #     return self.cube
    #
    # def moveRight(self):
    #     c = copy.deepcopy(self.cube)
    #     rightCol = 2
    #     for row in range(3):
    #         self.cube[row][rightCol] = c[4*row+4][rightCol]
    #     self.cube[4][rightCol] = c[15][rightCol]
    #     self.cube[8][rightCol] = c[16][rightCol]
    #     self.cube[12][rightCol] = c[17][rightCol]
    #     self.cube[6][rightCol] = c[2][rightCol]
    #     self.cube[10][rightCol] = c[1][rightCol]
    #     self.cube[14][rightCol] = c[0][rightCol]
    #     self.cube[15][rightCol] = c[14][rightCol]
    #     self.cube[16][rightCol] = c[10][rightCol]
    #     self.cube[17][rightCol] = c[6][rightCol]
    #     self.rotateRightFace()
    #     return self.cube
    #
    # def rotateLeftFace(self):
    #     # 3, 7, 11 are the rows for the left face
    #     cube = self.cube
    #     face = [cube[3], cube[7], cube[11]]
    #     f = [cube[3][:], cube[7][:], cube[11][:]]
    #     print(face)
    #     for row in range(3):
    #         for col in range(0, 3, 2):
    #             face[row][col] = f[2-col][row]
    #     return self.cube
    #
    # def moveLeft(self):
    #     leftCol = 0
    #

    def __repr__(self):
        return str(self.cube)

    def __eq__(self, other):
        return isinstance(other, Cube) and self.cube == other.cube



def makeMoves(cube, algorithm):
    # implements the moves in the algorithm
    # cube must be a Cube type
    assert(type(cube) == Cube)
    for move in algorithm:
        if move == "R":
            cube.turnRight()
        elif move == "U":
            cube.turnUp()
        elif move == "L":
            cube.turnLeft()
        elif move == "D":
            cube.turnDown()
        elif move == "B":
            cube.turnBack()
        elif move == "F":
            cube.turnFront()
        elif move == "R'":
            cube.turnRight()
            cube.turnRight()
            cube.turnRight()
        elif move == "U'":
            cube.turnUp()
            cube.turnUp()
            cube.turnUp()
        elif move == "L'":
            cube.turnLeft()
            cube.turnLeft()
            cube.turnLeft()
        elif move == "D'":
            cube.turnDown()
            cube.turnDown()
            cube.turnDown()
        elif move == "B'":
            cube.turnBack()
            cube.turnBack()
            cube.turnBack()
        elif move == "F'":
            cube.turnFront()
            cube.turnFront()
            cube.turnFront()
        elif move == "R2":
            cube.turnRight()
            cube.turnRight()
        elif move == "U2":
            cube.turnUp()
            cube.turnUp()
        elif move == "L2":
            cube.turnLeft()
            cube.turnLeft()
        elif move == "D2":
            cube.turnDown()
            cube.turnDown()
        elif move == "B2":
            cube.turnBack()
            cube.turnBack()
        elif move == "F2":
            cube.turnFront()
            cube.turnFront()
        elif move == "y":
            cube.rotateYaxis()
        elif move == "y'":
            cube.rotateYaxis()
            cube.rotateYaxis()
            cube.rotateYaxis()
        elif move == "y2":
            cube.rotateYaxis()
            cube.rotateYaxis()
    return algorithm

def testMoves():
    s = copy.deepcopy(solved)
    cube = Cube(s)
    print("Testing Right Turn...", end="")
    cube.turnRight()
    cube.turnRight()
    cube.turnRight()
    cube.turnRight()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Left Turn...", end="")
    cube.turnLeft()
    cube.turnLeft()
    cube.turnLeft()
    cube.turnLeft()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Up Turn...", end="")
    cube.turnUp()
    cube.turnUp()
    cube.turnUp()
    cube.turnUp()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Down Turn...", end="")
    cube.turnDown()
    cube.turnDown()
    cube.turnDown()
    cube.turnDown()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Front Turn...", end="")
    cube.turnFront()
    cube.turnFront()
    cube.turnFront()
    cube.turnFront()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Back Turn...", end="")
    cube.turnBack()
    cube.turnBack()
    cube.turnBack()
    cube.turnBack()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Solve...", end="")
    moves = "RRURURRRUUURRRUUURRRURRR"
    for move in moves:
        if move == "R":
            cube.turnRight()
        elif move == "U":
            cube.turnUp()
    assert(str(cube) != str(solved))
    print("Scrambled...", end="")
    solution = "RUUURURURUUURRRUUURR"
    for move in solution:
        if move == "R":
            cube.turnRight()
        elif move == "U":
            cube.turnUp()
    assert(str(cube) == str(solved))
    print("Passed!")

    print("Testing Rotate Y-Axis...", end="")
    cube.rotateYaxis()
    cube.rotateYaxis()
    cube.rotateYaxis()
    cube.rotateYaxis()
    assert(str(cube) == str(solved))
    print("Passed!")


testMoves()