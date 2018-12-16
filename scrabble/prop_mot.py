import glob
def propose_mot(msg_position_ligne, msg_position_colonne, msg_direction, msg_mot):
    """Cette fonction demande au joueur où et quel mot
    il desire placer.
    La sequence d'inputs et de verification
    est la suivante:
    1. Demander le numero de la ligne de la
    premiere lettre du mot a placer. Utilisez comme
    argument de la fonction input() : msg_position_ligne
    1.1 Tant que le joueur n'entre pas un numero de ligne valide
    (un caractere convertible en un nombre entier compris entre 0
    et NB_lIGNE-1), retourner en 1.
    2. Demander le numero de la colonne de la
    premiere lettre du mot a placer. Utilisez comme
    argument de la fonction input() : msg_position_colonne
    2.1 Tant que le joueur n'entre pas un numero de colonne valide(un caractere
    convertible en un nombre entier compris entre 0 et NB_COLONNE-1),
    retourner en 2.
    3. Demander la direction du mot a placer ("h" ou "v"). Utilisez comme
    argument de la fonction input() : msg_direction
    3.1 Tant que le joueur n'entre pas une direction valide(le caractere "h" ou "v"),
    retourner en 3.
    4. Demander le mot a placer. Utilisez comme
    argument de la fonction input() : msg_mot
    4.1 Tant que le joueur n'entre pas un mot valide(uniquement des lettres en majuscule
    ou minuscule), retourner en 4.
    Attention, si le mot a placer s'appuie sur une ou
    plusieurs lettres presentes sur le plateau, il faut
    preciser tout le mot qui sera forme et pas seulement
    les lettres a placer. Par exemple, partons de la situation
    initial suivante:
    plateau = [["_", "_", "_"], ["_", "_", "S"],["_", "_", "_"]]
    lettres = ['A','N','Z','Y','W','U','V']
    Si on veut placer le mot "ANS" avec les lettres "A", "N",
    a la position (1,0), avec comme direction "h"
    il faut proposer le mot "ANS" et non pas "AN" a placer.
    De même, imaginons que nous partons de la deuxieme situation
    initiale suivante :
    plateau = [["_", "_", "_","_"], ["D", "_", "_", "_"],["E","_", "_", "_"]]
    lettres = ['A','N','S','Y','W','U','V']
    Si on veut placer le mot "ANS" avec les lettres "A", "N","S",
    a la position (1,1), avec comme direction "h". Le mot final sera "DANS".
    Il faut alors proposer "DANS" comme mot, et non pas "ANS".
    Arguments :
    - msg_position_ligne (str) : une chaine de caractere a afficher a l'ecran
    du joueur lors de l'input pour lui demander quelle est le numero
    de ligne de la premiere lettre de son mot.
    - msg_position_colonne (str) : une chaine de caractere a afficher a l'ecran
    du joueur lors de l'input pour lui demander quelle est le numero
    de colonne de la premiere lettre de son mot.
    - msg_direction (str) : une chaine de caractere a afficher a l'ecran
    du joueur lors de l'input pour lui demander quelle est la
    direction pour son mot ("h" = horizontale ou "v" = verticale)
    - msg_mot (str) : une chaine de caractere a afficher a l'ecran
    du joueur lors de l'input pour lui demander quel mot le joueur
    desire placer
    Valeurs de retour (dans cet ordre):
    - (str): une chaine de caractere en MAJUSCULE qui indique le mot a placer
    - tuple: un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
    et le numero de la colonne (c) de la premiere lettre du mot a placer
    - (str): un charactere ("h" ou "v") qui indique la direction du mot
    """
    ligne = 0
    colonne = 0
    while not( 0 < ligne <= glob.NB_LIGNES):
        try:
            nombre = int(input(msg_position_ligne))
            ligne = nombre
        except ValueError:
            print ("veuillez entrer un nombre valide")
            continue


    while not( 0 < colonne <= glob.NB_COLONNES):
        try:
            nombre = int(input(msg_position_colonne))
            colonne = nombre
        except ValueError:
            print ("veuillez entrer un nombre valide")
            continue


    dir = str(input(msg_direction))
    dir = dir.lower()
    while not (dir == "h" or  dir == "v"):
        dir = str(input(msg_direction))
        dir = dir.lower()
    mot = str(input(msg_mot))
    mot = mot.upper()
    while not(mot.isalpha()):
        mot = str(input(msg_mot))
        mot = mot.upper()
    return mot, (ligne-1, colonne-1), dir
