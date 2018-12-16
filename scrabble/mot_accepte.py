from verif_bornes import verif_bornes
from verif_emplacement import verif_emplacement
from verif_lettres_joueur import verif_lettres_joueur
from verif_mot import verif_mot
from verif_pre_tour import verif_premier_tour
from verif_connect import utilise_lettre_plateau
from mots_perpendiculaires import mots_perpendiculaires
def mot_accepte(plateau, lettres_joueur, coup, dictionnaire, tour):
    """Cette fonction renvoie True si chacune des fonctions suivantes renvoient True:
    verif_premier_tour (uniquement au premier tour)
    verif_lettres_joueur
    verif_mot
    verif_bornes
    verif_emplacement
    Sinon, la fonction renvoie False. Vous devez donc egalement definir les 5 fonctions ci- dessus pour pouvoir les appeler dans votre fonction mot_accepte(plateau, lettres_joueur, coup, dictionnaire, tour). Attention l'ordre de verification de chacune de ces fonctions n'est pas anodin selon les hypothese faites pour chacune de ces fonctions. Par exemple, verif_emplacement pre-suppose que le mot ne depasse pas des bornes du plateau.
    Arguments :
    - lettres_joueur (liste) : une liste contenant les lettres du joueur
    - plateau (liste): une liste de sous-listes qui representent
    chacune une ligne du plateau de jeu.
    Elles contiennent chacune, soit un underscore pour
    indiquer que la case est vide, soit une lettre
    si elle a deja ete placee la auparavant.
    - coup (tuple): un tuple a 3 elements:
    - mot (str): une chaine de caractere en majuscule qui indique le mot a placer
    - pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
    et le numero de la colonne (c) de la premiere lettre du mot a placer
    - dir (str) : un charactere (h ou v) qui indique la direction du mot
    - tour (int) : un entier qui represente le tour du jeu (tour = 1 represente le premier tour)
    - dictionnaire (list) : une liste dont chaque element d'indice i, est un set de mots du dictionnaire de
    longueur (i+1). Par exemple, dico[3] pointe vers un set de tous les mots a 4 lettres.
    Valeurs de retour:
    - bool (True ou False)
    """
    mot, pos ,direction = coup
    dimensions = (len(plateau),len(plateau[0]))
    reponse = False
    if tour == 1:
        if verif_bornes(coup, dimensions):
            if verif_lettres_joueur(plateau, lettres_joueur, coup):
                if verif_mot(mot, dictionnaire):
                    if verif_premier_tour(coup):
                        reponse = True

    else :
        print("ok")
        if verif_bornes(coup, dimensions):
            print("ok")
            if verif_lettres_joueur(plateau, lettres_joueur, coup):
                print("ok")
                if verif_mot(mot, dictionnaire):
                    print("ok")
                    if utilise_lettre_plateau(coup, plateau):
                        reponse = True
                    elif len(mots_perpendiculaires(mots_perpendiculaires(coup,plateau,dico))) != 1:
                        reponse = True
    return reponse
