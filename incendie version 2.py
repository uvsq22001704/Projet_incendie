
########################
# Groupe 2 LDDMP
# Arthur CHAUVEAU
# Noémie KAUFMANN
# Titouan BIGET
# Diary ANDRIANARIVO
# Mohammed IBOUROI
# Hyacinthe MORASSE
# https://github.com/uvsq22001704/Projet_incendie
########################

########################
# import des librairies

import tkinter as tk
import random as rd

########################
# Constantes

COULEUR_FOND = "grey100"
COULEUR_QUADR = "grey50"
COULEUR_VIVANT = "yellow"
LARGEUR = 1600
HAUTEUR = 800
# la longueur des carrés qui constituent le quadrillage
COTE = 40
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE
COULEUR = ["dodger blue", "green yellow", "green4"]

######################
# Variables globales

tableau = None

########################
# fonctions

def terrain_aléatoire():
    '''crée un terrain aléatoire et place l'état des cases dans un tableau'''
    global tableau
    tableau = []
    ### Création du terrain aléatoire ###
    ### range la couleur dans une liste 2D [ligne] [cologne] ###
    for i in range(20):
        for j in range(40):
            tableau.append([])
            col = rd.choice(COULEUR)
            tableau[j].append(col)
            canvas.create_rectangle((j * COTE), (i * COTE), ((j+1) * COTE, (i+1) * COTE), fill = col)
    #print_tableau()
    
def quadrillage():
    """Affiche un quadrillage sur le canvas."""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE


def coord_to_lg(x, y):
    """Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y"""
    return x // COTE, y // COTE


def change_carre(event):
    """Change l'état du carré sur lequel on a cliqué"""
    i, j = coord_to_lg(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle(x, y, x + COTE,
                                        y + COTE, fill=COULEUR_VIVANT,
                                        outline=COULEUR_QUADR)
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = -1


def Alum_feu(event):
    """ donne l'état feu à la case clickée """

    #réccupere les coordonées du click
    x = event.x
    y = event.y
    x_border_1, y_border_1, x_border_2, y_border_2 = Coord_Case(x, y)

    #print (x, y)
    #print (tableau [y_border_1 // 40][x_border_2 // 40])

    #place le feu dans le canvenas et la liste 2D
    if tableau [y_border_1 // 40][x_border_2 // 40] != "dodger blue" and tableau [y_border_1 // 40][x_border_2 // 40] != "firebrick3":
        canvas.create_rectangle(x_border_1 + 40, y_border_1, x_border_2 + 40, y_border_2, fill = "firebrick3")
        tableau [y_border_1 // 40][x_border_1 // 40 + 1] = "firebrick3"


def Coord_Case(Coord_x, Coord_y):
    '''définie les bordures du x_border_1, x_border_2, y_border_1 & y_border_2 '''

    if (Coord_x < 1600 and Coord_y < 800):

        x_1= ((Coord_x-40) // 40)*40
        y_1 = (Coord_y // 40)*40
        y_2 = y_1 + 40
        x_2 = x_1 + 40
        
        return x_1, y_1, x_2, y_2
     


########################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)
quadrillage()


button1 = tk.Button(racine, text = "TERRAIN ALÉATOIRE", command = terrain_aléatoire)
button2 = tk.Button(racine, text = "SAUVEGARDE DU TERRAIN")
button3 = tk.Button(racine, text = "CHARGER UN TERRAIN")
button4 = tk.Button(racine, text = "ÉTAPE DE SIMULATION")
button5 = tk.Button(racine, text = "DÉMARRER LA SIMULATION")
button6 = tk.Button(racine, text = "ARRÊTER LA SIMULATION")

racine.bind("<Button-1>", Alum_feu)

# placement des widgets
canvas.grid(column=0, row=0, columnspan=3)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)
# liaison des événements
canvas.bind("<Button-1>", change_carre)
# boucle principale
racine.mainloop()


