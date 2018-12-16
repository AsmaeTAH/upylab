def plateau_init(dimensions):
    """Cette fonction va creer le plateau
    de jeu. Le plateau de jeu consiste
    en une liste de nb_lignes sous-listes,
    chacune de longueur nb_colonnes, où
    chaque element represente une case
    du plateau grâce a la valeur "_"
    (underscore).
    Si nb_lignes = nb_colonnes = 3, on aura
    par exemple:
    plateau = [["_", "_", "_"], ["_", "_", "_"],["_", "_", "_"]]
    Arguments:
    - dimensions (tuple) : un tuple de deux nombres
    entiers et positifs. Le premier element est le
    nombre de lignes (nb_lignes (int)) et le deuxieme
    element est le nombre de colonnes (nb_colonnes (int))
    Valeur de retour:
    - liste: la liste de sous-listes qui represente le plateau
    """
    sous_liste =  []
    lignes, colonnes = dimensions
    liste = [["_" for x in range(dimensions[1])] for y in range(dimensions[0])]
    return liste
