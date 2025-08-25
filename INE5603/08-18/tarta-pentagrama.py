import turtle

tarta = turtle.Turtle()
x = 100

tarta.left(108)
tarta.right(180)

for i in range(5):
    tarta.right(36)
    tarta.forward(x)
    tarta.right(180)

turtle.done()
