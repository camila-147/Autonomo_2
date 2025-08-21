

"""
Desarrollo de Software - Snake Game 🐍
Autora: Camila Pillajo

 Bienvenido al clásico Snake Game, ahora desarrollado como parte de un proyecto de software interactivo.

 📜 Reglas del Juego

   🚀 Misión: Controla a tu serpiente, cómete todas las manzanas y crece sin parar.
   💥 Cuidado: No choques contra los muros ni contra ti misma… ¡o la partida habrá terminado! :(
   🏆 Puntaje: Cada manzana suma puntos y aumenta el score . 
   🔥 Desafío: Mantente en movimiento, piensa rápido y demuestra que eres la mejor controlando a la serpiente.

 📌 Meta final: sobrevivir el mayor tiempo posible y alcanzar la máxima puntuación sin colisionar.

 ¿Estás listo para romper el récord?
 🎯 Come. Crece. Sobrevive.

 Mucha suerte.  :)

"""

import turtle
import time
import random
import tkinter as tk

# ========================
# VARIABLES GLOBALES
# ========================
score = 0
high_score = 0
manzanas_comidas = 0
delay = 0.1

# ========================
# VENTANA DE INICIO
# ========================
def iniciar_menu():
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Snake Game - Iniciar")
    ventana_inicio.geometry("300x200")
    ventana_inicio.resizable(False, False)

    etiqueta = tk.Label(ventana_inicio, text="¡Comenzar a jugar - Snake Game!", font=("Helvetica", 14))
    etiqueta.pack(pady=20)

    boton_iniciar = tk.Button(
        ventana_inicio,
        text=" 🐍 - START GAME - 🐍 ",
        font=("Helvetica", 12),
        command=lambda: [ventana_inicio.destroy(), jugar_snake()]
    )
    boton_iniciar.pack()

    ventana_inicio.mainloop()


# ========================
# FUNCIÓN: JUEGO PRINCIPAL
# ========================
def jugar_snake():
    global score, high_score, manzanas_comidas, delay
    score = 0
    manzanas_comidas = 0

    # Ventana Turtle
    ventana_turtle = turtle.Screen()
    ventana_turtle.title(" 🐍  Snake Game  🐍 ")
    ventana_turtle.bgcolor("black")
    ventana_turtle.setup(width=600, height=600)
    ventana_turtle.tracer(0)

    # Cabeza
    cabeza = turtle.Turtle()
    cabeza.speed(0)
    cabeza.shape("square")
    cabeza.color("lime")
    cabeza.penup()
    cabeza.goto(0, 0)
    cabeza.direction = "stop"

    # Comida
    comida = turtle.Turtle()
    comida.speed(0)
    comida.shape("circle")
    comida.color("red")
    comida.penup()
    comida.goto(0, 150)

    # Segmentos
    segmentos = []

    # Texto de puntaje
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("white")
    texto.penup()
    texto.hideturtle()
    texto.goto(0, 260)
    texto.write(f"Puntaje: {score}  |  Récord: {high_score}", align="center", font=("Courier", 20, "bold"))

    # Direcciones
    def ir_arriba():
        if cabeza.direction != "down":
            cabeza.direction = "up"

    def ir_abajo():
        if cabeza.direction != "up":
            cabeza.direction = "down"

    def ir_izquierda():
        if cabeza.direction != "right":
            cabeza.direction = "left"

    def ir_derecha():
        if cabeza.direction != "left":
            cabeza.direction = "right"

    # Movimiento
    def mover():
        if cabeza.direction == "up":
            cabeza.sety(cabeza.ycor() + 20)
        elif cabeza.direction == "down":
            cabeza.sety(cabeza.ycor() - 20)
        elif cabeza.direction == "left":
            cabeza.setx(cabeza.xcor() - 20)
        elif cabeza.direction == "right":
            cabeza.setx(cabeza.xcor() + 20)

    # Controles
    ventana_turtle.listen()
    ventana_turtle.onkeypress(ir_arriba, "Up")
    ventana_turtle.onkeypress(ir_abajo, "Down")
    ventana_turtle.onkeypress(ir_izquierda, "Left")
    ventana_turtle.onkeypress(ir_derecha, "Right")

    # ========================
    # BUCLE PRINCIPAL
    # ========================
    jugando = True
    while jugando:
        ventana_turtle.update()

        # Colisión con bordes
        if abs(cabeza.xcor()) > 290 or abs(cabeza.ycor()) > 290:
            jugando = False
            break

        # Colisión con comida
        if cabeza.distance(comida) < 20:
            comida.goto(random.randint(-290, 290), random.randint(-290, 290))

            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color("green")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)

            score += 10
            manzanas_comidas += 1
            high_score = max(high_score, score)

            texto.clear()
            texto.write(f"Puntaje: {score}  |  Récord: {high_score}", align="center", font=("Courier", 20, "bold"))

        # Mover cuerpo
        for index in range(len(segmentos) - 1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos[index - 1].ycor()
            segmentos[index].goto(x, y)

        if segmentos:
            segmentos[0].goto(cabeza.xcor(), cabeza.ycor())

        mover()

        # Colisión con cuerpo
        for segmento in segmentos:
            if segmento.distance(cabeza) < 20:
                jugando = False
                break

        time.sleep(delay)

    # Fin del juego 
    ventana_turtle.bye()
    mostrar_game_over()


# ========================
# FUNCIÓN: PANTALLA FINAL
# ========================
def mostrar_game_over():
    global score, high_score, manzanas_comidas

    ventana_Fin = tk.Tk()
    ventana_Fin.title("Fin del Juego")
    ventana_Fin.geometry("300x200+200+50") 
    ventana_Fin.resizable(False, False)

    etiqueta = tk.Label(ventana_Fin, text=" - GAME OVER -", font=("Courier", 18, "bold"))
    etiqueta.pack(pady=10)

    tk.Label(ventana_Fin, text=f"Puntaje: {score}", font=("Helvetica", 12)).pack()
    tk.Label(ventana_Fin, text=f"Récord: {high_score}", font=("Helvetica", 12)).pack()
    tk.Label(ventana_Fin, text=f"Manzanas comidas: {manzanas_comidas}", font=("Helvetica", 12)).pack()

    tk.Button(ventana_Fin, text=" ❌ Salir ", command=ventana_Fin.destroy).pack(pady=10)

# Ejecutar el juego 
iniciar_menu()
