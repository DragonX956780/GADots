import PlayerNN
import random as r

class GeneticAlgo:
    def __init__(self, population, goal):
        self.population = population
        self.goal = goal

    def fitness(self, goal):
        self.distance = []
        for p in self.population:
            self.distance.append(p.distToGoal(goal.g))

    def parentSelection(self, numMax):
        #says max but really smallest distance to goal, i just didn't wanna rename
        max = [9999 for n in range(numMax)]
        maxIndex = []
        best = []
        for d in range(len(self.distance)):
            max.sort()
            if self.distance[d] <= max[0]:
                max[0] = self.distance[d]
                maxIndex.append(d)
        
        for i in maxIndex[-(numMax+1):-1]:
            best.append(self.population[i])
        return best

    def makeKids(self, parents):
        parent1 = r.choice(parents)
        parent2 = r.choice(parents)
        child = PlayerNN.Network(2, 4)
        
        layerLoop = min(len(parent1.hidden), len(parent2.hidden))
        for i in range(layerLoop):
            winningParent = parent1 if r.randint(0, 1) == 0 else parent2
            child.addHiddenLayer(winningParent.hidden[i][0].weights, winningParent.hidden[i][0].bias)
            nodeLoop = min(len(parent1.hidden[i]), len(parent2.hidden[i]))

            for k in range(1, nodeLoop):
                winningParent = parent1 if r.randint(0, 1) == 0 else parent2
                child.addHiddenNode(i, winningParent.hidden[i][k].weights, winningParent.hidden[i][k].bias)

            if r.randint(0, 1) == 0:
                bigParent = parent1 if max(len(parent1.hidden[i]), len(parent2.hidden[i])) == len(parent1.hidden[i]) else parent2
                smallParent =  parent2 if max(len(parent1.hidden[i]), len(parent2.hidden[i])) == len(parent1.hidden[i]) else parent1
                difference = len(bigParent.hidden[i]) - len(smallParent.hidden[i])

                for k in range(difference):
                    whichOneToAdd = len(bigParent.hidden[i]) - 1 - difference + k #check if error
                    child.addHiddenNode(i, bigParent.hidden[i][whichOneToAdd])

        if r.randint(0, 1) == 0:
            bigParent = parent1 if max(len(parent1.hidden), len(parent2.hidden)) == len(parent1.hidden) else parent2
            smallParent = parent2 if max(len(parent1.hidden), len(parent2.hidden)) == len(parent1.hidden) else parent1
            difference = len(bigParent.hidden) - len(smallParent.hidden)

            for i in range(difference):
                whichOneToAdd = len(bigParent.hidden) - 1 - difference + i
                child.hidden.append(bigParent.hidden[whichOneToAdd])

        return child

    def mutate(self):
        pass
