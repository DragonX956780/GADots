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
output = [0, 1, 2, 3] #up, down, left, right

players = [Player() for i in range(2)]
playerBrains = [PlayerNN.Network(2, 4) for i in range(len(players))]

alg = ga(players, goal)

alg.fitness(goal)
t.tracer(1)

alg.parentSelection(2)

playerBrains[0].addHiddenLayer()
playerBrains[0].addHiddenLayer()
playerBrains[1].addHiddenLayer()
playerBrains[1].addHiddenNode(0)

playerBrains[0].addHiddenNode(0)
playerBrains[0].addHiddenNode(0)
playerBrains[0].addHiddenNode(0)
playerBrains[0].addHiddenNode(0)


mutation = alg.mutate(thing)

t.done()