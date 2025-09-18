import turtle

tarta = turtle.Turtle()
tarta.speed(50)

for lado in range(30, 200):
    tarta.left(92)
    tarta.forward(lado)

turtle.done()
