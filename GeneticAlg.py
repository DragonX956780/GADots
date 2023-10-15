from Game.DotsToGoal import Player
from Game.DotsToGoal import Goal
import turtle as t

players = []
goal = Goal()

lifeSpan = 15

currentLoc = (0, 0)
goalLoc = (0, 0)

input = [currentLoc, goalLoc]
output = [0, 1, 2, 3] #up, down, left, right

players = [Player() for i in range(100)]




t.done()