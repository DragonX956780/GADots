import PlayerNN
import random as r

class GeneticAlgo:
    def __init__(self, population, goal, populationBrain):
        self.population = population
        self.populationBrain = populationBrain
        self.goal = goal

    def updateBrains(self, brains):
        self.populationBrains = brains
    
    def updatePlayers(self, players):
        self.population = players
    
    def fitness(self, goal, population):
        self.distance = []
        for p in population:
            self.distance.append(p.distToGoal(goal.g))

    def parentSelection(self, numMax):
        #says self.max but really smallest distance to goal, i just didn't wanna rename
        self.max = [9999 for n in range(numMax)]
        self.maxIndex = []
        self.best = []
        for d in range(len(self.distance)):
            self.max.sort(reverse = True)
            if self.distance[d] <= self.max[0]:
                self.max[0] = self.distance[d]
                self.maxIndex.append(d)
        
        for i in self.maxIndex[-(numMax+1):-1]:
            self.best.append(self.populationBrain[i])
        
        print(self.max)
        return self.best

    def makeKids(self, parents):
        self.parent1 = r.choice(parents)
        self.parent2 = r.choice(parents)
        self.child = PlayerNN.Network(2, 4)
        
        self.layerLoop = min(len(self.parent1.hidden), len(self.parent2.hidden))
        for i in range(self.layerLoop):
            self.winningParent = self.parent1 if r.randint(0, 1) == 0 else self.parent2
            self.child.addHiddenLayer(self.winningParent.hidden[i][0].weights, self.winningParent.hidden[i][0].bias)
            self.nodeLoop = min(len(self.parent1.hidden[i]), len(self.parent2.hidden[i]))

            for k in range(1, self.nodeLoop):
                self.winningParent = self.parent1 if r.randint(0, 1) == 0 else self.parent2
                self.child.addHiddenNode(i, self.winningParent.hidden[i][k].weights, self.winningParent.hidden[i][k].bias)

            #maybe add extra nodes
            if r.randint(0, 1) == 0:
                self.bigParent = self.parent1 if max(len(self.parent1.hidden[i]), len(self.parent2.hidden[i])) == len(self.parent1.hidden[i]) else self.parent2
                self.smallParent =  self.parent2 if max(len(self.parent1.hidden[i]), len(self.parent2.hidden[i])) == len(self.parent1.hidden[i]) else self.parent1
                self.difference = len(self.bigParent.hidden[i]) - len(self.smallParent.hidden[i])

                for k in range(self.difference):
                    self.whichOneToAdd = len(self.bigParent.hidden[i]) - 1 - self.difference + k #check if error
                    self.child.addHiddenNode(i, self.bigParent.hidden[i][self.whichOneToAdd].weights, self.bigParent.hidden[i][self.whichOneToAdd].bias)

        #maybe add extra layers
        if r.randint(0, 1) == 0:
            self.bigParent = self.parent1 if max(len(self.parent1.hidden), len(self.parent2.hidden)) == len(self.parent1.hidden) else self.parent2
            self.smallParent = self.parent2 if max(len(self.parent1.hidden), len(self.parent2.hidden)) == len(self.parent1.hidden) else self.parent1
            self.difference = len(self.bigParent.hidden) - len(self.smallParent.hidden)

            for i in range(self.difference):
                self.whichOneToAdd = len(self.bigParent.hidden) - 1 - self.difference + i
                for d in range(self.whichOneToAdd, len(self.bigParent.hidden)):
                    self.child.addHiddenLayer(self.bigParent.hidden[self.whichOneToAdd][0].weights, self.bigParent.hidden[self.whichOneToAdd][0].bias)
                    for l in range(1, len(self.bigParent.hidden[self.whichOneToAdd])):
                        self.child.addHiddenLayer(self.bigParent.hidden[self.whichOneToAdd][l].weights, self.bigParent.hidden[self.whichOneToAdd][l].bias)

        return self.child

    def mutate(self, kid):
        self.kid = kid
        for i in range(len(self.kid.hidden)):
            for k in range(len(self.kid.hidden[i])):
                for w in range(len(self.kid.hidden[i][k].weights)):
                    #change
                    self.kid.hidden[i][k].weights[w] = r.random() if r.randint(0, 1000) == 0 else self.kid.hidden[i][k].weights[w]
                    #kill
                    self.kid.hidden[i][k].value = 0 if r.randint(0,1000) == 0 else self.kid.hidden[i][k].value

                self.kid.hidden[i][k].bias = r.random() if r.randint(0, 1000) == 0 else self.kid.hidden[i][k].bias

        for o in range(len(self.kid.output)):
            for w in range(len(self.kid.output[o].weights)):
                self.kid.output[o].weights[w] = r.random() if r.randint(0, 1000) == 0 else self.kid.output[o].weights[w]
            self.kid.output[o].bias = r.random() if r.randint(0, 1000) == 0 else self.kid.output[o].bias

        return self.kid
            
