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

HEIGHT = 800
WIDTH = 1600
PARCEL_HEIGHT = HEIGHT / 20
PARCEL_WIDTH = WIDTH / 40
DUREE_FEU = 0
DUREE_CENDRE = 0
color = ["dodger blue", "green yellow", "green4"]
itemiser = [] #liste 2D dans laquelle les couleurs sont rangées

######################


######################
# Défintion des variables globales

COMPTEUR = 0

######################


######################
# Défintion des fonctions

def terrain_aléatoire():
    global itemiser
    itemiser = []
    ### Création du terrain aléatoire ###
    ### range la couleur dans une liste 2D [colone] [ligne] ###
    for i in range(40):
        for j in range(20):
            itemiser.append([])
            col = rd.choice(color)
            itemiser[j].append(col)
            canvas.create_rectangle((i * PARCEL_WIDTH), (j * PARCEL_HEIGHT), ((i+1) * PARCEL_WIDTH, (j+1) * PARCEL_HEIGHT), fill = col)
    print_itemiser()
    
    print (itemiser[5][1])

def sauvegarde():
    ### Sauvegarde du terrain ###
    canvas.postscript(file="incendie.eps", colormode="color")

def refresh():
    ### actualise la map ###
    global itemiser
    for i in range(40):
        for j in range(20):
            canvas.create_rectangle((i * PARCEL_WIDTH), (j * PARCEL_HEIGHT), ((i+1) * PARCEL_WIDTH, (j+1) * PARCEL_HEIGHT), fill = itemiser[j][i])


def print_itemiser():
    for i in range(20):
        print ( "line", i, itemiser[i])
        print (" ")


def START_FIRE(event):
    """ donne l'état feu à la case clickée """
        #réccupere les coordonées du click
    Coord_x = event.x
    Coord_y = event.y
    
        
        #définie les bordures du x_border_1, x_border_2, y_border_1 & y_border_2 
    if (Coord_x < 1600 and Coord_y < 800):

        x_border_1= (Coord_x // 40)*40
        y_border_1 = (Coord_y // 40)*40

        if x_border_1>= Coord_x:
            x_border_2 = x_border_1- 40
            if y_border_1 >= Coord_y:
                y_border_2 = y_border_1 - 40
            else:
                y_border_2 = y_border_1 + 40
        else:
            x_border_2 = x_border_1+ 40
            if y_border_1 >= Coord_y:
                y_border_2 = y_border_1 - 40
            else:
                y_border_2 = y_border_1 + 40

        #place le feu dans le canvenas et la liste 2D
    if itemiser [Coord_y // 40][Coord_x // 40] != "dodger blue":
        canvas.create_rectangle(x_border_1, y_border_1, x_border_2, y_border_2, fill = "purple")
        itemiser [Coord_y // 40][Coord_x // 40] = "purple"

    #print_itemiser()

######################



######################
# Programme principal
root = tk.Tk ()
root.title("Simulation d'un incendie")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
button1 = tk.Button(root, text = "TERRAIN ALÉATOIRE", command=terrain_aléatoire)
button2 = tk.Button(root, text = "SAUVEGARDE DU TERRAIN", command=sauvegarde)
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

root.bind("<Button-1>", START_FIRE)

root.mainloop ()

######################