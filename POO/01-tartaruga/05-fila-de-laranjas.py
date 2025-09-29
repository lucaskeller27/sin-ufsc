# import turtle, math

# tarta = turtle.Turtle()
# tarta.speed(50)

# def bola(raio):
#     tarta.color("orange")
#     tarta.begin_fill()
#     tarta.circle(raio)
#     tarta.end_fill()

# razao = 10

# for raio in range(10, 70, razao):
    
#     bola(raio)
    
#     d = math.sqrt((2 * raio + razao) ** 2 - razao ** 2)
    
#     tarta.up()
#     tarta.forward(d)
#     tarta.down()

# turtle.done()

# Importar o módulo Turtle
import turtle

# Criar uma variável para a tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(20)

# Desenhar a fila de laranjas
razao = 10
for n in range(0, 6, razao):
    tartaruga.dot(100, "orange")
