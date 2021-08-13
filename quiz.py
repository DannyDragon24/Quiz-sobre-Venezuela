from os import stat
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root = Tk()
root.geometry("600x500+400+100")
root.resizable(0,0)
root.title("Quiz Venezuela")
respuestas_correctas = 0
respuestas_incorrectas = 0


#PANTALLA PRINCIPAL
im = ImageTk.PhotoImage(Image.open("salto.png").resize((600,500)))
canvas = Canvas(root,width=600,height=500)
canvas.pack(fill=BOTH,expand=True)
canvas.create_image(0,0,image=im,anchor="nw",tags="imagen")
canvas.create_text(300,100,text="Bienvenido",font=("Arial",56),fill="yellow",tags="text1")
canvas.create_text(300,250,text="Este es un pequeño quiz para probar\n tu conocimiento sobre Venezuela",font=("Arial",20),fill="white",tags="text2")
#CERRAR PROGRAMA
def cerrar():
    root11.destroy()
#PANTALLA DE RESULTADOS
def resultados_screen():
    root10.destroy()
    global root11
    root11 = Tk()
    root11.geometry("600x500+400+100")
    root11.resizable(0,0)
    root11.config(bg="light gray")
    root11.title("Quiz Venezuela")
    label_resultados = Label(root11,text="RESULTADOS",font=("Arial",30),bg="light gray")
    label_resultados.grid(row=0,column=0,padx=180,pady=50)
    label_respuestas_correctas = Label(root11,text=f"Respuestas correctas: {respuestas_correctas}",font=("Arial",15),bg="light gray",fg="green")
    label_respuestas_correctas.grid(row=1,column=0,pady=30)
    label_respuestas_incorrectas = Label(root11,text=f"Respuestas incorrectas: {respuestas_incorrectas}",font=("Arial",15),bg="light gray",fg="red")
    label_respuestas_incorrectas.grid(row=2,column=0,pady=30)
    boton_cerrar = Button(root11,text="Cerrar",width=11,height=2,font=("Arial",20),command=cerrar)
    boton_cerrar.grid(row=3,column=0,pady=40)
#DECIMA PREGUNTA
def pregunta10_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root9.destroy()
    #VARIABLES
    global root10
    root10 = Tk()
    root10.geometry("600x500+400+100")
    root10.resizable(0,0)
    root10.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 1:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 2 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        resultados_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("cueva.jpg").resize((600,500)))
    Pantalla1 = Canvas(root10,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="La caverna Charles Brewer también\n se le conoce como...",font=("Arial",24),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root10,text="Cueva de El Fantasma",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root10,text="Cueva Charlie",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root10,text="Caverna escondida",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root10.mainloop()
#NOVENA PREGUNTA
def pregunta9_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root8.destroy()
    #VARIABLES
    global root9
    root9 = Tk()
    root9.geometry("600x500+400+100")
    root9.resizable(0,0)
    root9.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 3:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 2 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta10_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("mendoza.jpg").resize((600,500)))
    Pantalla1 = Canvas(root9,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿Nombre del primer presidente de Venezuela?",font=("Arial",21),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root9,text="Simon Bolivar",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root9,text="Francisco de Miranda",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root9,text="Cristóbal Mendoza",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root9.mainloop()
#OCTAVA PREGUNTA
def pregunta8_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root7.destroy()
    #VARIABLES
    global root8
    root8 = Tk()
    root8.geometry("600x500+400+100")
    root8.resizable(0,0)
    root8.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 2:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 1 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta9_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("golpe.jpg").resize((600,500)))
    Pantalla1 = Canvas(root8,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿En que año fue el primer golpe\n de estado de Hugo Chávez?",font=("Arial Black",25),fill="blue")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root8,text="1988",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root8,text="1992",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root8,text="1995",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root8.mainloop()
#SEPTIMA PREGUNTA
def pregunta7_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root6.destroy()
    #VARIABLES
    global root7
    root7 = Tk()
    root7.geometry("600x500+400+100")
    root7.resizable(0,0)
    root7.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 2:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 1 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta8_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("miranda.jpg").resize((600,500)))
    Pantalla1 = Canvas(root7,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿En que año murió Francisco de Miranda?",font=("Arial Black",19),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root7,text="1820",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root7,text="1816",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root7,text="1810",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root7.mainloop()

#SEXTA PREGUNTA
def pregunta6_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root5.destroy()
    #VARIABLES
    global root6
    root6 = Tk()
    root6.geometry("600x500+400+100")
    root6.resizable(0,0)
    root6.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 2:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 1 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta7_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("angel.jpg").resize((600,500)))
    Pantalla1 = Canvas(root6,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿Como se llama la cascada más alta del\n mundo ubicada en Venezuela?",font=("Arial",21),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root6,text="Cataratas del Niagaras",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root6,text="Salto Ángel",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root6,text="Cataratas Kaleteur",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root6.mainloop()
#QUINTA PREGUNTA
def pregunta5_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root4.destroy()
    #VARIABLES
    global root5
    root5 = Tk()
    root5.geometry("600x500+400+100")
    root5.resizable(0,0)
    root5.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 1:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 2 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta6_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("hotel.jpg").resize((600,500)))
    Pantalla1 = Canvas(root5,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿Nombre del hotel en la cima del Cerro Ávila?",font=("Arial",21),fill="black")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root5,text="Humbolt",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root5,text="Tamanco",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root5,text="Hilton",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root5.mainloop()
#CUARTA PREGUNTA
def pregunta4_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root3.destroy()
    #VARIABLES
    global root4
    root4 = Tk()
    root4.geometry("600x500+400+100")
    root4.resizable(0,0)
    root4.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 1:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 2 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta5_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("teleferico.jpg").resize((600,500)))
    Pantalla1 = Canvas(root4,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿En que estado queda el teleférico más alto del mundo?",font=("Arial",17),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root4,text="Mérida",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root4,text="Yaracuy",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root4,text="Zulia",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root4.mainloop()
#TERCERA PREGUNTA
def pregunta3_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root2.destroy()
    #VARIABLES
    global root3
    root3 = Tk()
    root3.geometry("600x500+400+100")
    root3.resizable(0,0)
    root3.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 3:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 1 or respuesta_opcion.get() == 2:
            respuestas_incorrectas += 1
        pregunta4_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("Chichiriviche.jpg").resize((600,500)))
    Pantalla1 = Canvas(root3,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿En que estado queda el pueblo Chichiriviche?",font=("Arial",21),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root3,text="Bolivar",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root3,text="Barinas",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root3,text="Falcón",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root3.mainloop()
#SEGUNTA PREGUNTA
def pregunta2_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root1.destroy()
    #VARIABLES
    global root2
    root2 = Tk()
    root2.geometry("600x500+400+100")
    root2.resizable(0,0)
    root2.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 1:
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 2 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1
        pregunta3_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("simon.png").resize((600,500)))
    Pantalla1 = Canvas(root2,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿En que año murió Simon Bolivar?",font=("Arial",25),fill="white")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root2,text="1830",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root2,text="1890",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root2,text="1820",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root2.mainloop()
#PRIMERA PREGUNTA
def pregunta1_screen():
    #DESTRUIR PANTALLA ANTERIOR
    root.destroy()
    #VARIABLES
    global root1
    root1 = Tk()
    root1.geometry("600x500+400+100")
    root1.resizable(0,0)
    root1.title("Quiz Venezuela")
    global respuesta_opcion
    respuesta_opcion = IntVar()
    #FUNCION PARA OBTENER VALORES DE RADIOBUTTONS
    def obtener_valores():
        global respuestas_correctas
        global respuestas_incorrectas
        if respuesta_opcion.get() == 2:  
            respuestas_correctas += 1
        elif respuesta_opcion.get() == 1 or respuesta_opcion.get() == 3:
            respuestas_incorrectas += 1 
        pregunta2_screen()
    #DIBUJAR IMAGEN Y TEXTO EN LA PANTALLA
    imagen1 = ImageTk.PhotoImage(Image.open("caracas.png").resize((600,500)))
    Pantalla1 = Canvas(root1,width=600,height=500)
    Pantalla1.pack(fill=BOTH,expand=True)
    Pantalla1.create_image(0,0,image=imagen1,anchor="nw")
    Pantalla1.create_text(300,100,text="¿Cómo se llama la ciudad capital de Venezuela?",font=("Arial",19),fill="yellow")
    #RADIOBUTTONS
    respuesta1 = Radiobutton(root1,text="Mérida",font=("Arial",15),variable=respuesta_opcion,value=1,command=obtener_valores)
    respuesta1_radio = Pantalla1.create_window(100,200,anchor="nw",window=respuesta1)
    respuesta2 = Radiobutton(root1,text="Caracas",font=("Arial",15),variable=respuesta_opcion,value=2,command=obtener_valores)
    respuesta2_radio = Pantalla1.create_window(100,250,anchor="nw",window=respuesta2)
    respuesta3 = Radiobutton(root1,text="Maracaibo",font=("Arial",15),variable=respuesta_opcion,value=3,command=obtener_valores)
    respuesta3_radio = Pantalla1.create_window(100,300,anchor="nw",window=respuesta3)
    root1.mainloop()

#BOTON PARA COMENZAR EL QUIZ
boton_comenzar = Button(root,text="Comenzar",width=11,height=2,font=("Arial",20),command=pregunta1_screen)
boton_canvas = canvas.create_window(210,320,anchor="nw",window=boton_comenzar)
root.mainloop()
