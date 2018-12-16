import glob
def placer_mot(coup,plateau, lettres_joueur):
    """ Cette fonction modifie le plateau de
    sorte que les lettres du mot a placer soient
    inserees au bon endroit dans la liste de
    sous-listes qui represente le plateau;
    cette fonction renvoie ensuite les lettres du mot
    a placer qui sont deja presentes sur le plateau
    a l'endroit exact où cette lettre devrait etre
    placee (et qu'il ne faut donc pas retirer du
    chevalet du joueur par la suite)
    Arguments:
        - coup (tuple): un tuple a 3 elements:
            - mot (str): une chaine de caractere en majuscule qui indique le mot a placer
            - pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
            et le numero de la colonne (c) de la premiere lettre du mot a placer
            - dir (str) : un charactere (h ou v) qui indique la direction du mot
            - plateau (liste) : une liste de sous-listes
            qui representent chacune une ligne du plateau
            de jeu. Elles contiennent chacune, soit un
            underscore pour indiquer que la case est vide,
            soit une lettre si elle a deja ete placee la
            auparavant.
        Valeur de retour:
            - str : chaine de caracteres contenant les lettres deja presentes sur le plateau a
            l'emplacement du mot (qu'il ne faut donc pas retirer du chevalet du joueur)
        Exemple:
    >>> plateau = [["_", "_", "A","R"],
                    ["_", "_", "_","_"],
                    ["_", "_", "_","_"],
                    ["_", "_", "_","_"]]
    >>> mot = "BAR"
    >>> position = (0,1)
    >>> direction = "h"
    >>> coup = mot,position,direction
    >>> lettres_presentes = placer_mot(plateau,coup)
    >>> print(plateau)
    >>> [["_", "B", "A","R"],
    ["_", "_", "_","_"],
    ["_", "_", "_","_"],
    ["_", "_", "_","_"]]
    >>> print(lettres_presentes)
    >>> "AR"
    """
    mot, pos ,direction = coup
    hor,ver = pos
    liste_mot = []
    reponse = ""
    liste_mot = list()
    for i in mot:
        liste_mot.append(str(i))
    if direction == "h":
        count = 0
        for i in liste_mot:
            if glob.plateau[hor][ver+count] == i:
                reponse +=i
            else:
                if i in lettres_joueur:
                    lettres_joueur.remove(i)
                elif "*" in lettres_joueur:
                    lettres_joueur.remove("*")
            glob.plateau[hor][ver+count] = i

            count +=1
    else:
        count = 0
        for i in liste_mot:
            if glob.plateau[hor+count][ver] == i:
                reponse +=i
            else:
                lettres_joueur.remove(i)
            glob.plateau[hor+count][ver] = i
            count+=1
    return reponse
