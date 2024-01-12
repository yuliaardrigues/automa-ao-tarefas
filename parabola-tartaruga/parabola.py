import turtle

COLORES = ['yellow','green']

def generar_linea(x, y):
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto(x, 0)
    
def dibujar_parabola():
    for y in range(-280, 281, 8):
        index = abs(y)// 8 %len(COLORES)
        turtle.pencolor(COLORES[index])
        x = (y + 280)* 0.8 if y < 0 else (280 - y) * 0.8
        generar_linea(x, y)
        generar_linea(-x, y)
        
turtle.speed('fastest')
turtle.bgcolor('black')

dibujar_parabola()

turtle.hideturtle()
turtle.done()