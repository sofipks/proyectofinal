import tkinter as tk
from random import shuffle
import pygame

pygame.mixer.init() 
musica = pygame.mixer.Sound("musiquita.mp3")
musica.play() 

sonido_boton = pygame.mixer.Sound("boton.mp3")

preguntas = [
    "¿En qué fecha fue la batalla de Salta?",
    "¿En el camino a qué lugar se encuentra la Quebrada de las Conchas?",
    "¿Cuándo fue la fundación de Salta?",
    "¿Quién fue Martín Miguel de Güemes?",
    "¿Qué era Macacha Güemes de Martín Miguel?",
    "¿En qué lugar cercano a la ciudad de Salta se encuentran selvas de Yungas?",
    "¿A dónde nos lleva el teleférico?",
    "¿Quién compuso la zamba de Balderrama, la pomeña y zamba del carnaval?",
    "¿Qué quebrada del norte es patrimonio cultural y natural de la humanidad?",
    "¿Cuándo falleció Güemes?"
]

respuestas = [
    ["20 de febrero de 1813", "20 de agosto de 1811", "9 de julio de 1816"],
    ["Cafayate", "Cachi", "Cerrillos"],
    ["16 de abril de 1582", "30' de abril de 1682", "22 de mayo de 1584"],
    ["Héroe nacional de la independencia Argentina", "Caudillo", "Presidente de la Nación Argentina"],
    ["Su hermana", "Su hija", "Su mamá"],
    ["San Lorenzo", "San Luis", "San Antonio de los Cobres"],
    ["A la cima del cerro San Bernardo", "A la cima de la Quebrada de Humahuaca", "A la cima del cerro del autódromo"],
    ["El Cuchi Leguizamón y Manuel J. Castilla", "Los Nocheros y Los Tekis", "Mercedes Sosa y Horacio Guarany"],
    ["La Quebrada de Humahuaca", "La Quebrada del Toro", "La Quebrada de las Conchas"],
    ["17 de junio de 1821", "17 de noviembre de 1831", "10 de julio de 1821"]
]

respuestas_correctas = [
    "20 de febrero de 1813",
    "Cafayate",
    "16 de abril de 1582",
    "Héroe nacional de la independencia Argentina",
    "Su hermana",
    "San Lorenzo",
    "A la cima del cerro San Bernardo",
    "El Cuchi Leguizamón y Manuel J. Castilla",
    "La Quebrada de Humahuaca",
    "17 de junio de 1821"
]

def cargar_pregunta():
    pregunta_text.set(preguntas[current_question])
    shuffle(respuestas[current_question])
    for i in range(3):
        botones_respuestas[i].config(text=respuestas[current_question][i])

def verificar_respuesta(respuesta_usuario):
    sonido_boton.play()
    global puntaje, current_question
    if respuestas[current_question][respuesta_usuario] == respuestas_correctas[current_question]:
        puntaje += 1
    else:
        respuestas_incorrectas.append(f"{preguntas[current_question]}: Respondiste '{respuestas[current_question][respuesta_usuario]}', la respuesta correcta es '{respuestas_correctas[current_question]}'")
    current_question += 1
    if current_question < len(preguntas):
        cargar_pregunta()
    else:
        mostrar_resultado()

def mostrar_resultado():
    mensaje_adicional = ""
    if puntaje == 10:
        mensaje_adicional = "¡Perfecto! ¡Sabes mucho de Salta!"
    elif puntaje >= 7:
        mensaje_adicional = "¡Buen trabajo!"
    elif puntaje >= 5:
        mensaje_adicional = "¡No está mal!"
    else:
        mensaje_adicional = "Presta más atención para la próxima..."

    resultado_text.set(f"Obtuviste un puntaje de {puntaje}/10\n{mensaje_adicional}")
    
    respuestas_incorrectas_text.set("Respuestas en las que te equivocaste:\n" + "\n".join(respuestas_incorrectas))

root = tk.Tk()
root.title("Cuestionario Salta")
root.iconbitmap("cactuslogo.ico")
root.configure(bg="skyblue")

pregunta_text = tk.StringVar()
pregunta_label = tk.Label(root, textvariable=pregunta_text, font=("Cambria", 14), bg="mintcream", fg="midnightblue")
pregunta_label.pack(pady=30)

botones_respuestas = []
for i in range(3):
    respuesta_button = tk.Button(root, text="", command=lambda i=i: verificar_respuesta(i), bg="cadetblue")
    respuesta_button.pack(pady=5)
    botones_respuestas.append(respuesta_button)

respuestas_incorrectas = []
respuestas_incorrectas_text = tk.StringVar()
respuestas_incorrectas_label = tk.Label(root, textvariable=respuestas_incorrectas_text, font=("Cambria", 12), bg="lightsteelblue")
respuestas_incorrectas_label.pack(pady=10)

resultado_text = tk.StringVar()
resultado_label = tk.Label(root, textvariable=resultado_text, font=("Cambria", 14), bg="lightsteelblue")
resultado_label.pack(pady=20)

puntaje = 0
current_question = 0

cargar_pregunta()

root.mainloop()
