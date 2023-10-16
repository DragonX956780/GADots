from Game.DotsToGoal import Player
from Game.DotsToGoal import Goal
import PlayerNN
from GeneticAlg import GeneticAlgo as ga
import turtle as t
import time
import random as r

t.tracer(0)
players = []
goal = Goal()

lifeSpan = 15

currentLoc = (0, 0)
goalLoc = (250, 0)

input = [currentLoc, goalLoc]
output = [0, 1, 2, 4] #0, 1, 2, 3 = up, down, left, right

numPlayers = 10
players = [Player() for i in range(numPlayers)]
# players = [Player()]
playerBrains = [PlayerNN.Network(7, 4) for i in range(len(players))]
directions = [[0, 0, 0, 0] for i in range(numPlayers)]
alg = ga(players, goal, playerBrains)

# for i in range(10):
#     for b in playerBrains:
#         move = b.forwardPass((players[0].distToGoal(goal.g), players[0].getX(), players[0].getY()))
#         print(players[0].distToGoal(goal.g), players[0].getX(), players[0].getY())
#         if move == 0:
#             players[0].up()
#         if move == 1:
#             players[0].down()
#         if move == 2:
#             players[0].left()
#         if move == 3:
#             players[0].right()
#     time.sleep(0.2)

steps = 20
for a in range(100):
    t.tracer(0)
    for p in players:
        p.center()
    for k in range(steps):
        for i in range(len(players)):
            move = playerBrains[i].forwardPass((players[i].distToGoal(goal.g)/100.0, players[i].getX()/100, players[i].getY()/100, directions[i][0], directions[i][1], directions[i][2], directions[i][3]))
            if move == 0:
                players[i].up()
                directions[i] = [1, 0, 0, 0]
            if move == 1:
                players[i].down()
                directions[i] = [0, 1, 0, 0]
            if move == 2:
                players[i].left()
                directions[i] = [0, 0, 1, 0]
            if move == 3:
                players[i].right()
                directions[i] = [0, 0, 0, 1]

    numParents = 5
    alg.fitness(goal, players)
    parents = alg.parentSelection(numParents)
    children = []
    for j in range(numPlayers - numParents):
        children.append(alg.makeKids(parents))

    playerBrains.clear()

    for p in parents:
        playerBrains.append(p)
    for c in children:
        child = alg.mutate(c)
        playerBrains.append(child)

    for i in playerBrains:
        print(i.showNetwork())
    alg.updateBrains(playerBrains)
    # print(children[0].showNetwork())

    if(len(players) != len(playerBrains)):
        print("ERROR, PLAYERS AND BRAINS DON'T LINE UP")
        print(len(players))
        print(len(playerBrains), len(parents), len(children))
        quit()

    t.tracer(1)
    t.update()
    # steps += 2
    time.sleep(0.1)

print("DONE")
print(playerBrains[0].showNetwork())
t.done()