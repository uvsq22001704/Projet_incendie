######################
# Groupe 2 LDDMP
# Arthur CHAUVEAU
# Noémie KAUFMANN
# Titouan BIGET
# Diary ANDRIANARIVO
# Ibouroi MOHAMMED
# Hyacinthe MORASSE
# https://github.com/uvsq22001704/Projet_incendie
######################

######################
# Import des librairies

import tkinter as tk

######################


######################
# Définition des constantes
root = tk.Tk ()

HEIGHT = 800
WIDTH = 1600
PARCEL_HEIGHT = HEIGHT / 20
PARCEL_WIDTH = WIDTH / 40

######################


######################
# Défintion des variables globales


######################


######################
# Défintion des fonctions


######################


######################
# Programme principal

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
button1 = tk.Button(root, text = "B1")
button2 = tk.Button(root, text = "B2")
button3 = tk.Button(root, text = "B3")
button4 = tk.Button(root, text = "B4")
button5 = tk.Button(root, text = "B5")
button6 = tk.Button(root, text = "B6")


canvas.grid(column=0, row=0, columnspan=3)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)

######################


root.mainloop ()
