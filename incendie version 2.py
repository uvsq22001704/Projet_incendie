
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
import pickle as pk

########################
# Constantes

LARGEUR = 1600
HAUTEUR = 800
# la longueur des carrés qui constituent le quadrillage
COTE = 40
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE
COULEUR = ["dodger blue", "yellow2", "green4"]

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
        canvas.create_line(x0, y, x1, y, fill="grey")
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill="grey")
        x += COTE


def coord_to_lg(x, y):
    """Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y"""
    return x // COTE, y // COTE


def Alum_feu(event):
    """ donne l'état feu à la case clickée """

    #réccupere les coordonées du click
    x = event.x
    y = event.y
    x_border_1, y_border_1, x_border_2, y_border_2 = Coord_Case(x, y)

    #print (x, y)
    #print (tableau [y_border_1 // 40][x_border_2 // 40])

    #place le feu dans le canvenas et la liste 2D
    if tableau [x_border_2 // 40] [y_border_1 // 40]!= "dodger blue" and tableau[x_border_2 // 40] [y_border_1 // 40] != "firebrick3":
        canvas.create_rectangle(x_border_1 + 40, y_border_1, x_border_2 + 40, y_border_2, fill = "firebrick3")
        tableau [x_border_1 // 40 + 1] [y_border_1 // 40] = "firebrick3"

def refresh():
    '''### Construit la map à partir de tableau ###'''
    global tableau
    for i in range(20):
        for j in range(40):
            canvas.create_rectangle((j * COTE), (i * COTE), ((j+1) * COTE, (i+1) * COTE), fill = tableau[j][i])

def print_tableau():
    '''### print tableau dans le terminal column par coliumn ###'''
    for i in range(40):
        print ( "column", i, tableau[i])
        print (" ")

def sauvegarde():
    ''' Sauvegarde du terrain avec pickle dans un .txt; ce fichier est enregistré dans le même fichier que le .py du code '''

    global tableau
    fichier_de_sauvegarde = open("sauvegarde_terrain.txt", "wb") #crée un fichier nommé "sauvergarde_terrain.txt"
    pk.dump( tableau, fichier_de_sauvegarde) #écrit tableau dans le fichié

def charger():
    '''Récupère les données du fichier de sauvegarde et reconstruit le tableau et la map'''

    global tableau
    fichier_de_sauvegarde = open("sauvegarde_terrain.txt", 'rb') #cherche un fichier nommé "sauvergarde_terrain"
    tableau = pk.load(fichier_de_sauvegarde) # récupere des données du .txt et les met dans tableau
    #print_tableau()
    refresh()


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
canvas = tk.Canvas(racine, bg="white", width=LARGEUR, height=HAUTEUR)
quadrillage()


button1 = tk.Button(racine, text = "TERRAIN ALÉATOIRE", command = terrain_aléatoire)
button2 = tk.Button(racine, text = "SAUVEGARDE DU TERRAIN", command = sauvegarde)
button3 = tk.Button(racine, text = "CHARGER UN TERRAIN", command = charger)
button4 = tk.Button(racine, text = "ÉTAPE DE SIMULATION")
button5 = tk.Button(racine, text = "DÉMARRER LA SIMULATION")
button6 = tk.Button(racine, text = "ARRÊTER LA SIMULATION")


# placement des widgets
canvas.grid(column=0, row=0, columnspan=3)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)
# liaison des événements
canvas.bind("<Button-1>", Alum_feu)
# boucle principale
racine.mainloop()


