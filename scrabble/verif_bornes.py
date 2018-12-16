def verif_bornes(coup,dimensions):
    """Cette fonction renvoie True si le mot e placer ne
    depasse pas les des bornes du plateau de jeu. False, sinon.
    Arguments :
    - coup (tuple): un tuple e 3 elements:
    - mot (str): une chaine de caractere en majuscule qui indique le mot e placer
    - pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
    et le numero de la colonne (c) de la premiere lettre du mot e placer
    - dir (str) : un charactere (h ou v) qui indique la direction du mot
    - dimensions (tuple) : un tuple de deux nombres entiers et positifs. Le premier element est le nombre de lignes (nb_lignes); le deuxieme element est le nombre de colonnes (nb_colonnes)
    Valeurs de retour:
    - bool (True ou False)
    """
    x,y = dimensions
    mot, pos ,direction = coup
    hor,ver = pos
    reponse = bool()
    if direction == 'h':
        reponse = ver+len(mot)<=y

    else:
        reponse = hor+len(mot)<=x
    return reponse
