import turtle

tarta = turtle.Turtle()
tarta.speed(20)

for lado in range(10, 200, 5):
    tarta.forward(lado)
    tarta.right(90)

turtle.done()
