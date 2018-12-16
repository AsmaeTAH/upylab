"""
Jeu de scrabble
auteur:Ramdani Oualid
Date: 16 decembre 2018
Jeu de scrabble se jouant en multijoueurs avec un nombre de lignes et colonnes modulables

Entrees: nombre de lignes et de colonnes du plateau, le nombre de joueurs et leur noms ainsi que le coup joue a chaque tour
Sorties :
"""


"""
importation des differentes fonctions et fichiers
les seuls modules utilise est random (et turtle)
"""
from random import randint

from open_file import load_fichier_lettres
from mot_accepte import mot_accepte
from pioche_in import pioche_init
from placer_mot import placer_mot
from plateau_in import plateau_init
from prop_mot import propose_mot
from make_dico_list import make_dico_list
from creer_joueurs import creer_joueurs
from prop_dim import prop_dim
from compte_points import compte_points
from pioche_2 import pioche_2
from print_plateau import print_plateau
from mots_perpendiculaires import mots_perpendiculaires
from gagnant import gagnant


"""creation de constantes"""
import glob
tour = 1
rate =0 #cette variable compte le nombre de fautes faites en un seul tour pour pouvoir passer au tour suivant si une personne se trompe plusieurs fois


"""creation de dictionnaire et listes dependents de fichiers externes"""
occurences, valeurs = load_fichier_lettres("lettres.txt")
dico = make_dico_list("dico.txt")

"""creation du plateau"""
prop_dim()
glob.plateau = plateau_init((glob.NB_LIGNES, glob.NB_COLONNES))
print_plateau()

"""creation de joueurs"""
pioches_dispo = pioche_init(occurences)
joueurs = creer_joueurs(pioches_dispo)
encours = randint(0,len(joueurs)-1)
#enlever ce commentaires pour afficher tous les joueurs
#print(joueurs)







"""jeu principal"""
while len(pioches_dispo) != 0:
    if tour == 1:
        print("le premier mot doit passer par la ligne " +str((glob.NB_LIGNES//2)+1) + " et la colonne " + str((glob.NB_COLONNES//2)+1) )
    if encours == len(joueurs): #
        encours = 0



    print("c'est au tour de "+joueurs[encours][1])
    print("son chevalet est compose de " + str(joueurs[encours][2]))
    print("son score actuel est de " +str(joueurs[encours][3]) )




    coup = propose_mot("ligne ou commence votre mot ","colonne ou commence votre mot ","direction de votre mot ","le mot ")
    #print(coup)
    while not mot_accepte(glob.plateau,joueurs[encours][2], coup, dico,tour) and rate < 2:
        print("vous vous etes trompes:")
        print_plateau()
        print (joueurs[encours])
        rate +=1
        coup = propose_mot("ligne ou commence votre mot ","colonne ou commence votre mot ","direction de votre mot ","le mot ")
    rate = 0
    if mot_accepte(glob.plateau,joueurs[encours][2], coup, dico,tour):
        placer_mot(coup, glob.plateau,joueurs[encours][2])
        for i in mots_perpendiculaires(coup, glob.plateau, dico):
            joueurs[encours][3] += compte_points(i, valeurs)
        if len(joueurs[encours][2]) == 0 :
            joueurs[encours][3] +=50
        print_plateau()
        pioche_2(pioches_dispo,joueurs[encours][2])
        tour+=1
    encours +=1


"""decision du gagnant en fin de partie"""
idgagnant = gagnant(joueurs)
print("il n'y plus assez de pieces pour continuer a jouer, le gangnant est :" + str(joueurs[idgagnant][1]))
