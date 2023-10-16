import turtle as t

spawn = (-250,0)

class Player:
    def __init__(self):
        self.p = t.Turtle()
        self.p.shape("circle")
        self.p.shapesize(0.2)
        self.p.penup()
        self.p.goto(spawn)

    def right(self):
        self.p.goto(self.p.xcor() + 5, self.p.ycor())
    
    def left(self):
        self.p.goto(self.p.xcor() - 5, self.p.ycor())

    def up(self):
        self.p.goto(self.p.xcor(), self.p.ycor() + 5)

    def down(self):
        self.p.goto(self.p.xcor(), self.p.ycor() - 5)
    
    def center(self):
        self.p.goto(spawn)

    def distToGoal(self, goal):
        distance = ((goal.xcor() - self.p.xcor())**2 + (goal.ycor() - self.p.ycor())**2)**0.5
        return distance

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