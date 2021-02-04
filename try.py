from queue import Queue


def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze



def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

nums = Queue()
nums.put("")
add = ""
maze  = createMaze2()

while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)






## TRDL
# 5 8
# 1 0 1 1 0
# 2 0 1 1 1
# 3 0 1 0 1
# 4 0 0 1 1
# 5 0 1 1 0
# 6 0 1 1 1
# 7 0 1 0 1
# 8 0 0 1 1
# 9 1 1 1 0
# 10 1 0 0 1
# 11 0 1 0 0
# 12 1 0 1 1
# 13 1 0 1 0
# 14 1 1 0 0
# 15 0 0 1 1
# 16 1 0 1 0
# 17 1 0 1 0
# 18 0 1 1 0
# 19 0 1 0 1
# 20 1 0 1 1
# 28 1 0 1 0
# 29 1 0 1 0
# 30 1 0 1 0
# 31 0 1 1 0
# 32 0 0 1 1
# 33 1 1 0 0
# 34 0 0 0 1
# 35 1 0 0 0
# 36 1 1 0 0
# 37 1 0 0 1
# 38 1 1 0 0
# 39 0 1 0 1
# 40 1 0 0 11 1 0 1 0

