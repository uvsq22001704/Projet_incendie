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
import random as rd


######################


######################
# Définition des constantes
root = tk.Tk ()

HEIGHT = 800
WIDTH = 1600
PARCEL_HEIGHT = HEIGHT / 20
PARCEL_WIDTH = WIDTH / 40
DUREE_FEU = 
DUREE_CENDRE = 

######################


######################
# Défintion des variables globales

COMPTEUR = 0

######################


######################
# Défintion des fonctions


######################


######################
# Programme principal

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
button1 = tk.Button(root, text = "TERRAIN ALÉATOIRE")
button2 = tk.Button(root, text = "SAUVEGARDE DU TERRAIN")
button3 = tk.Button(root, text = "CHARGER UN TERRAIN")
button4 = tk.Button(root, text = "ÉTAPE DE SIMULATION")
button5 = tk.Button(root, text = "DÉMARRER LA SIMULATION")
button6 = tk.Button(root, text = "ARRÊTER LA SIMULATION")


canvas.grid(column=0, row=0, columnspan=3)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)

######################


root.mainloop ()
