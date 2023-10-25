from PlayerNN import Network as nn
from Game.DotsToGoal import Goal
from Game.DotsToGoal import Player
import random as r

player = Player()
mind = nn(1, 2)
goal = Goal()

mind.addHiddenLayer()

mind.addHiddenNode(0)
mind.addHiddenNode(0)
mind.addHiddenNode(0)
mind.addHiddenNode(0)
mind.addHiddenNode(0)

for i in range(20):
    input = player.distToGoal(goal.g)
    result = mind.forwardPass(input)
    for i in range(len(mind.output)):
        for w in range(len(mind.output[i].weights)):
            mind.output[i].weights[w] = 0.5
        mind.output[i].bias = 0
    if result == 0:
        player.left()
    if result == 1:
        player.right()
   print(mind.output[0].value, mind.output[1].value) 
