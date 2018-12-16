def utilise_lettre_plateau(coup, plateau):
    """
Cette fonction renvoie True si le mot e placer utilise une ou plusieurs lettres
deje presentes sur le plateau de jeu.
Elle renvoie False sinon
Arguments:
- coup (tuple) : e 3 elements :
- mot (str) : une chaine de caractere en majuscule
qui indique le mot e placer
- direction (str) : un charactere (h ou v) qui
indique la direction du mot
- position (tuple) : un tuple d'entiers (l,c) qui
indiquent le numero de ligne (l),
et le numero de la colonne (c) de la premiere lettre
du mot e placer
- plateau (liste) : une liste de 15 sous-listes
qui representent chacune une ligne du plateau
de jeu. Elles contiennent chacune, soit un
underscore pour indiquer que la case est vide,
soit une lettre si elle a deje ete placee le
auparavant.
- Valeurs de retour:
- bool (True / False)


cette fonction sert aussi a verifier qu'un coup ne se supperpose pas entierement sur un mot deja present sinon il est possible de 'placer' ce mot sans avoir de lettres dans le chevalet et gagner des points
"""

    mot, pos ,direction = coup
    hor,ver = pos
    liste_mot = []
    errors = 0
    ok = 0
    ok2 = 0
    if direction == "h":
        count = 0
        for i in mot:
            if (plateau[hor][ver+count] == i):
                ok+=1
            elif (plateau[hor][ver+count] == "_"):
                ok2 +=1
            count +=1
    else:
        count = 0
        for i in mot:
            if (plateau[hor+count][ver] == i):
                ok+=1
            elif (plateau[hor+count][ver] == "_"):
                ok2 +=1
            count +=1
    return ok !=0 and ok2 !=0
