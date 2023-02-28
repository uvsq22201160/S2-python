import tkinter as tk
import random as rd

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
cpt = 0
Bouton = [0]*2

def Disque():
    global cpt
    global Bouton
    canvas.delete('all')
    canvas.configure(bg="gray")
    x1, y1 = rd.randint(210,500), rd.randint(170, 500) 
    x2, y2 = x1+100, y1+100
    canvas.create_oval(x1, y1, x2, y2, fill="blue")
    Bouton[0].destroy()
    



dessin = tk.Tk()
dessin.title("Mon dessin")
frame = tk.Frame(dessin, width=800, height=800, bg="white")

canvas = tk.Canvas(dessin, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
canvas.grid(row=1, column=1, rowspan=9, columnspan=5)
Choisir_une_couleur = tk.Button(text="Choisir une couleur", font=("helevetica", '12'), bg="CadetBlue1").grid(row=0, column=3, pady=10)

Carre = tk.Button(text="Carré", font=("helevetica", '12'), bg="CadetBlue1").grid(row=5, column=0, padx=10)
Croix = tk.Button(text="Croix", font=("helevetica", '12'), bg="CadetBlue1")
Croix.grid(row=8, column=0, padx=10)

Bouton[0] = tk.Button(text="Cercle", font=("helevetica", '12'), bg="CadetBlue1", command=Disque)
Bouton[0].grid(row=2, column=0, padx=10)

if cpt >= 1:
    frame.delete('all')

dessin.mainloop()