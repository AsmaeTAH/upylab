def verif_emplacement(coup, plateau):
    """Cette fonction renvoie True si le mot e placer n'entre
    pas en conflit avec d'autres lettres deje placees
    auparavant sur le plateau, qui ne correspondent pas aux
    lettres du mot.
    Sinon, la fonction renvoie False.
    On pre-suppose que le mot ne depasse pas des bornes du plateau.
    Arguments :
    - coup (tuple): un tuple e 3 elements:
    - mot (str): une chaine de caractere en majuscule qui indique le mot e placer
    - pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
    et le numero de la colonne (c) de la premiere lettre du mot e placer
    - dir (str) : un charactere (h ou v) qui indique la direction du mot
    - plateau (liste): une liste de sous-listes qui representent
    chacune une ligne du plateau de jeu.
    Elles contiennent chacune, soit un underscore pour
    indiquer que la case est vide, soit une lettre
    si elle a deje ete placee le auparavant.
    Valeurs de retour:
    - bool (True ou False)"""
    mot, pos ,direction = coup
    hor,ver = pos
    liste_mot = []
    errors = 0
    for i in mot:
        liste_mot.append(i)
    if direction == "h":
        count = 0
        for i in liste_mot:
            if (plateau[hor][count+ver] == "_" or plateau[hor][count+ver] == i):
                count +=1
            else:
                errors +=1

    else:
        count = 0
        for i in liste_mot:
            if (plateau[count+hor][ver] == "_" or plateau[count+hor][ver] == i):
                count +=1
            else:
                errors +=1
    return errors ==0
