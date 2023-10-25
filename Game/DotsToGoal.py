import turtle as t

spawn = (-250,0)

class Player:
    def __init__(self):
        self.p = t.Turtle()
        self.p.shape("circle")
        self.p.shapesize(0.2)
        self.p.penup()
        self.p.goto(spawn)

    def left(self):
        self.p.left(5)
        self.p.forward(5)

    def right(self):
        self.p.right(5)
        self.p.forward(5)
    
    def respawn(self):
        self.p.goto(spawn)

    def distToGoal(self, goal):
        distance = ((goal.xcor() - self.p.xcor())**2 + (goal.ycor() - self.p.ycor())**2)**0.5
        return 1/(1+distance)

    def getX(self):
        return self.p.xcor()

    def getY(self):
        return self.p.ycor()


class Goal:
    def __init__(self):
        self.g = t.Turtle()
        self.g.penup()
        self.g.shape("circle")
        self.g.color("green")
        self.g.shapesize(0.5)
        self.g.goto(250,0)