from Game.DotsToGoal import Player
from Game.DotsToGoal import Goal
import PlayerNN
from GeneticAlg import GeneticAlgo as ga
import turtle as t

t.tracer(0)
players = []
goal = Goal()

lifeSpan = 15

currentLoc = (0, 0)
goalLoc = (250, 0)

input = [currentLoc, goalLoc]
output = [0, 1, 2, 4]

#0, 1, 2, 3 = up, down, left, right

players = [Player() for i in range(2)]
playerBrains = [PlayerNN.Network(2, 4) for i in range(len(players))]
alg = ga(players, goal)


t.tracer(0)
for a in range(200):
    steps = 10
    for k in range(steps):
        for i in range(len(playerBrains)):
            move = playerBrains[i].forwardPass()
            if move == 0:
                players[i].up()
            if move == 1:
                players[i].down()
            if move == 2:
                players[i].left()
            if move == 3:
                players[i].right()

    alg.fitness(goal)
    parents = alg.parentSelection(5)
    children = []
    for j in range(95):
        children.append(alg.makeKids(parents))

    playerBrains.clear()

    for p in parents:
        playerBrains.append(j)
    for c in children:
        child = alg.mutate(c)
        playerBrains.append(child)

    t.sleep(0.2)


t.done()