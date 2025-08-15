from tkinter import *

def abrir_ventana(titulo, mensaje):
    top = Toplevel(ventana)
    top.title(titulo)
    top.geometry("300x200")
    top.config(bg="black")

    Label(top, text=mensaje,
          bg="black", fg="white", font=("Arial", 12), wraplength=250).pack(pady=20)

    Button(top, text="Cerrar", command=top.destroy,
           bg="white", fg="black", font=("Arial", 10)).pack()

ventana = Tk()
ventana.title("Jhoasnel José Méndez Aguilar")
ventana.geometry("600x500")
ventana.resizable(False, False)
ventana.config(bg="black")

# Frame principal
frame_1 = Frame(ventana, bg="black", width=690, height=240)
frame_1.place(x=10, y=10)

# Logo opcional
# logo = PhotoImage(file="img/logo.png")
# Label_logo = Label(frame_1, image=logo)
# Label_logo.place(x=100, y=10)

# Título
titulo = Label(frame_1, text="Jhoasnel José Méndez Aguilar",
               bg="black", fg="white", font=("Arial", 16))
titulo.place(x=280, y=90)

# Subtítulo
subtitulo = Label(frame_1, text="APP DE YO",
                   bg="black", fg="white", font=("Arial", 15), anchor=CENTER)
subtitulo.place(x=360, y=120)

# Botones con nombres personalizados
btn1 = Button(ventana, text="Nacimiento", width=20,
              command=lambda: abrir_ventana("nacimiento", "17/09/2009"))
btn1.place(x=10, y=300)

btn2 = Button(ventana, text="Familia", width=20,
              command=lambda: abrir_ventana("Familia", "7 personas incluyendome"))
btn2.place(x=210, y=300)

btn3 = Button(ventana, text="Educacion", width=20,
              command=lambda: abrir_ventana("educacion", "donde e estudiado en mi vida"))
btn3.place(x=410, y=300)

btn4 = Button(ventana, text="amigos", width=20,
              command=lambda: abrir_ventana("amigos", "jesus y gallo"))
btn4.place(x=10, y=350)

btn5 = Button(ventana, text="hobbies", width=20,
              command=lambda: abrir_ventana("hobbies", "jugar futbol"))
btn5.place(x=210, y=350)

btn6 = Button(ventana, text="horario", width=20,
              command=lambda: abrir_ventana("horario", "ir a la escuela llego a mi casa y me voy hasta las 9:00 pm a la cancha hago la cena y me acuesto a dormir"))
btn6.place(x=410, y=350)

btn7 = Button(ventana, text="preparacion", width=20,
              command=lambda: abrir_ventana("preparacion", "voy a estudiar ungles"))
btn7.place(x=10, y=400)

btn8 = Button(ventana, text="proyecto", width=20,
              command=lambda: abrir_ventana("proyecto", "ser ingeniero en sistema"))
btn8.place(x=210, y=400)

ventana.mainloop()

