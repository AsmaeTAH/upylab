import glob
def verif_premier_tour(coup):
    """Cette fonction retourne True si le mot a placer passe bien par la case mediane du plateau.
    On considere que le mot a placer ne depasse pas des bornes du plateau
    et ne fait pas plus de 7 lettres. On considere egalement que cette fonction ne
    sera appelee qu'au premier tour. Le plateau est donc totalement vide.
    Arguments :
    - coup (tuple): un tuple a 3 elements:
    - mot (str): une chaine de caractere en majuscule qui indique le mot a placer
    - pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
    et le numero de la colonne (c) de la premiere lettre du mot a placer
    - dir (str) : un charactere (h ou v) qui indique la direction du mot
    Valeurs de retour :
    - bool : True ou False
    """
    milver = (glob.NB_LIGNES //2)
    milhor = (glob.NB_COLONNES//2)
    mot, pos ,direction = coup
    hor,ver = pos
    reponse = False
    if direction == "h":
        posi_change = ver
        if hor == milhor:
            for i in mot:
                if posi_change == milver:
                    reponse = True
                posi_change+=1
    else:
        posi_change = hor
        if ver == milver:
            for i in mot:
                if posi_change == milhor:
                    reponse = True
                posi_change+=1
    return reponse
