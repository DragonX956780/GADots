from Game.DotsToGoal import Player
from Game.DotsToGoal import Goal
import PlayerNN
from GeneticAlg import GeneticAlgo as ga
import turtle as t
import time

t.tracer(0)
players = []
goal = Goal()

lifeSpan = 15

currentLoc = (0, 0)
goalLoc = (250, 0)

input = [currentLoc, goalLoc]
output = [0, 1, 2, 4] #0, 1, 2, 3 = up, down, left, right

numPlayers = 100
players = [Player() for i in range(numPlayers)]
playerBrains = [PlayerNN.Network(3, 4) for i in range(len(players))]
alg = ga(players, goal, playerBrains)


t.tracer(0)
for a in range(200):
    t.tracer(0)
    steps = 20
    for p in players:
        p.center()
    for k in range(steps):
        for i in range(len(players)):
            move = playerBrains[i].forwardPass((players[i].distToGoal(goal.g) * 0.02, players[i].getX() * 0.01, players[i].getY() * 0.01))
            if move == 0:
                players[i].up()
            if move == 1:
                players[i].down()
            if move == 2:
                players[i].left()
            if move == 3:
                players[i].right()

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

    alg.updateBrains(playerBrains)

    if(len(players) != len(playerBrains)):
        print("ERROR, PLAYERS AND BRAINS DON'T LINE UP")
        print(len(players))
        print(len(playerBrains), len(parents), len(children))
        quit()
    t.tracer(1)
    t.update()
    steps += 2
    time.sleep(0.2)


t.done()