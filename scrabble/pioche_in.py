def pioche_init(occurences_lettres):
    """ Cette fonction renvoie une chaine de
    caracteres (str) contenant toutes les
    lettres disponibles lors de
    l'initialisation du jeu, classees dans l'ordre alphabetique.
    Arguments:
    - occurences_lettres (dict) : dictionnaire ayant comme cles
    toutes les lettres de l'alphabet
    et comme valeur, le nombre de fois (int)
    que chaque lettre devra être ajoutee
    a la pioche
    Valeur de retour:
    - str : une chaine de caractere contenant toutes les lettres de la pioche classees dans l'ordre
    alphabetique.
    """
    items = occurences_lettres.items()
    liste = []
    for i in items:
        for b in range(i[1]) :
            liste.append(i[0])
    liste.sort()
    return liste
