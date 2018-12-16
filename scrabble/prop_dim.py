import glob
from turtle import *

def prop_dim():
    """cette fonction sert a prendre des input impaires et differents de 1"""
    NB_LIGNES = 2
    NB_COLONNES = 2
    while NB_LIGNES%2 == 0 or NB_LIGNES == 1:
        try:
            nombre = input("veuillez entrer un nombre impaire de lignes:  ")
            nombre = int(nombre)
            if nombre == 42:
                turtle = Turtle()
                turtle.write("la vie, l'univers et tout le reste",align="center", font=("arial", 20, "normal"))
            NB_LIGNES = nombre
        except ValueError:
            print ("veuillez entrer un nombre valide")
            continue

    while NB_COLONNES%2 == 0 or NB_COLONNES == 1:
        try:
            nombre = input("veuillez entrer un nombre impaire de colonnes:  ")
            nombre = int(nombre)
            NB_COLONNES = nombre
        except ValueError:
            print ("veuillez entrer un nombre valide")
            continue
    glob.NB_COLONNES = NB_COLONNES
    glob.NB_LIGNES = NB_LIGNES
