# Second Lab Eval AI  Question 1
from math import e
from random import randint

t = 500  # initial temprature
tc = 50  # cooling rate


def heuristic(a, b, c, d) -> int:
    temp = 0
    if not a or d:  # (¬a u d)
        temp += 1
        # print("1st")
    if c or b:  # (c u b)
        temp += 1
        # print("2nd")
    if not c or not d:  # (¬c u ¬d)
        temp += 1
        # print("3rd")
    if not d or not b:  # ( ¬d u ¬b)
        temp += 1
        # print("4th")
    if not a or not d:  # (¬a u ¬d)
        temp += 1
        # print("5th")
    return temp


def movegen(a, b, c, d) -> list:
    rand = randint(0, 3)
    # print(a,b,c,d)
    temp = [a, b, c, d]
    temp[rand] = not temp[rand]
    # print(temp)
    # print(rand)
    return temp
    # [a,b,c,d]=temp
    # print(a,b,c,d)


a = b = c = d = True
oldHeuristic = heuristic(a, b, c, d)

while t > 0:
    # print(t)
    newState = movegen(a, b, c, d)
    newHeuristic = heuristic(newState[0], newState[1], newState[2], newState[3])
    if (newHeuristic - oldHeuristic) > 0:
        [a, b, c, d] = newState
        oldHeuristic = newHeuristic
    else:
        # print("check move")
        p = e ** ((newHeuristic - oldHeuristic) / t)
        if p > 0.5:
            [a, b, c, d] = newState
            oldHeuristic = newHeuristic
    t -= 50
    # if newHeuristic == 5:
    #     break

print(a, b, c, d, "\nHeuristic value is:", heuristic(a, b, c, d))
