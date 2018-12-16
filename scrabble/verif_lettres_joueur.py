def verif_lettres_joueur(plateau, lettres_joueur, coup):
    """
    Cette fonction renvoie True:
    - Si le mot a placer appartient aux lettres du joueur (lettres_joueurs)
    ou
    - Si une ou plusieurs lettres manquent mais sont deja placees a la place
    adequate sur le plateau (plateau).
    Sinon, la fonction renvoie False.
    On pre-suppose que le mot ne depasse pas des bornes du plateau
    Arguments :
    - plateau (liste) : une liste de sous-listes qui representent
    chacune une ligne du plateau de jeu.
    Elles contiennent chacune, soit un underscore pour
    indiquer que la case est vide, soit une lettre
    si elle a deja ete placee la auparavant.
    - lettres_joueur (liste) : une liste qui contient chacune
    des lettres que le joueur possede sur son chevalet.
    Toutes ces lettres sont en MAJUSCULE.
    - coup (tuple): un tuple a 3 elements:
    - mot (str): une chaine de caractere en majuscule qui indique le mot a placer
    - pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
    et le numero de la colonne (c) de la premiere lettre du mot a placer
    - dir (str) : un charactere (h ou v) qui indique la direction du mot
    Valeurs de retour:
    - bool (True ou False)
    """

    mot, pos ,direction = coup
    hor,ver = pos
    liste_mot = []
    errors = 0
    count = 0
    lettres = list(lettres_joueur)
    if direction == "h":
        for i in mot:
            if plateau[hor][ver+count] == '_':
                if i in lettres:
                    lettres.remove(i)
                elif "*" in lettres:
                    lettres.remove("*")
                else:
                    errors +=1
            elif plateau[hor][ver+count] == i:
                pass
            else:
                errors +=1
            count +=1
    if direction == "v":
        for i in mot:
            if plateau[hor+count][ver] == '_':
                if i in lettres:
                    lettres.remove(i)
                elif "*" in lettres:
                    lettres.remove("*")
                else:
                    errors +=1
            elif plateau[hor+count][ver] == i:
                pass
            else:
                errors +=1
            count +=1
    return errors == 0
