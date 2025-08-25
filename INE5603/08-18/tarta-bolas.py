import turtle, math

tarta = turtle.Turtle()
tarta.speed(50)

def bola(raio):
    tarta.color("orange")
    tarta.begin_fill()
    tarta.circle(raio)
    tarta.end_fill()

razao = 10

for raio in range(10, 70, razao):
    
    bola(raio)
    
    d = math.sqrt((2 * raio + razao) ** 2 - razao ** 2)
    
    tarta.up()
    tarta.forward(d)
    tarta.down()

turtle.done()
