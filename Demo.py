import turtle

t = turtle.Turtle()
t.pensize(5)
colors = ["blue", "black", "red", "yellow", "green"]
positions = [(-120, 0), (0, 0), (120, 0), (-60, -50), (60, -50)]

t.speed(3)
for color, pos in zip(colors, positions):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.color(color)
    t.circle(50)

t.hideturtle()
turtle.done()
