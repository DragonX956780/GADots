import random as r

class InputNode:
    def __init__(self):
        self.value = 0

class OutputNode:
    def __init__(self, numIncoming, weights = None, bias = None):
        self.value = 0
        self.bias = bias
        if self.bias == None:
            self.bias = r.random()
        self.weights = weights
        if self.weights == None:
            self.weights = [r.random() for n in range(numIncoming)]

class HiddenNode:
    def __init__(self, numOfInputs, weights = None, bias = None):
        self.value = 0
        self.bias = bias
        if self.bias == None:
            self.bias = r.random()
        self.weights = weights
        if self.weights == None:
            self.weights = [r.random() for n in range(numOfInputs)]

class Network:
    def __init__(self, numInput, numOutput):
        self.input = [InputNode() for n in range(numInput)]
        self.hidden = []
        self.output = [OutputNode(numInput) for n in range(numOutput)]

    def addHiddenLayer(self, weights = None, bias = None):
        if len(self.hidden) == 0:
            self.hidden.append([HiddenNode(len(self.input), weights, bias)])
        else:
            self.hidden.append([HiddenNode(len(self.hidden[-1]), weights, bias)])
            for o in range(len(self.output)):
                self.output[o].weights = [r.random()]

    def addHiddenNode(self, layer, weights = None, bias = None):
        if len(self.hidden) == 0:
            self.addHiddenLayer()            
        else:
            self.lenInputs = len(self.hidden[layer-1]) if layer != 0 else len(self.input)
            self.hidden[layer].append(HiddenNode(self.lenInputs, weights, bias))

            #update weights in all nodes in next layer
            if layer == len(self.hidden) - 1:
                 for o in range(len(self.output)):
                    self.output[o].weights.append(r.random())               
            else:
                for h in range(len(self.hidden[layer+1])):
                    self.hidden[layer+1][h].weights.append(r.random())

    def delHiddenNode(self, layer, node):
        self.hidden[layer][node].value = 0 

    def forwardPass(self):
        #for the first pass with no hidden
        if (len(self.hidden) == 0):
            for o in range(len(self.output)):
                tempOutput = 0
                for i in range(len(self.input)):
                    tempOutput += self.input[i].value * \
                        self.output[o].weights[i]

                self.output[o].value = tempOutput + self.output[o].bias
                #print(self.output[o].value)
        else:
            total = len(self.hidden) + 1
            for l in range(total):
                if (l != total - 1):
                    for h in range(len(self.hidden)):
                        if h == 0:
                            for hh in range(len(self.hidden[h])):
                                temp = 0
                                for i in range(len(self.input)):
                                    temp += self.input[i].value * \
                                        self.hidden[h][hh].weights[i]
                                self.hidden[h][hh].value = temp + \
                                    self.hidden[h][hh].bias
                        else:
                           for hh in range(len(self.hidden[h])):
                               temp = 0
                               for hv in range(len(self.hidden[h-1])):
                                    temp += self.hidden[h-1][hv].value * self.hidden[h][hh].weights[hv]
                               self.hidden[h][hh].value = temp + self.hidden[h][hh].bias
                else:
                    for o in range(len(self.output)):
                        tempOutput = 0
                        for h in range(len(self.hidden[-1])):
                            tempOutput += self.hidden[-1][h].value * self.output[o].weights[h]

                        self.output[o].value = tempOutput + self.output[o].bias
                        #print(self.output[o].value) 

#hidden = [[], [], []] an n amount of times, so loop through each
#hidden is of dynamic size
