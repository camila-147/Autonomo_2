"CAMILA PILLAJO"

# Importaciones
import turtle
import time
import random

# Configuración inicial de la ventana
wn = turtle.Screen()
wn.title("Snake Game - Estructuras de Decisión y Bucles")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactiva actualizaciones automáticas

# Configuración de la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo de la serpiente
segmentos = []

# Marcador
score = 0

# Texto del puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntaje: 0", align="center", font=("Courier", 24, "normal"))