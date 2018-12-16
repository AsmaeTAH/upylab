def compte_points(mots, points_lettres):
    """Cette fonction calcule et renvoie le score
    associe a un mot
    Arguments :
    - mot (str) : une chaine de caractere en majuscule qui indique le mot a placer
    - points_lettres (dict) : un dictionnaire contenant
    comme cles les differentes lettres de l'alphabet,
    en majuscule; et comme valeur, les points
    associees a chaque lettre.
    Par exemple:
    points_lettres = {"A" : 1, "B": 3}, si on ne considere
    que les deux premieres lettres de l'alphabet
    Valeur de retour:
    - int : points associes au mot place.
    """
    somme = 0
    for i in mots:
        somme += points_lettres.get(i)
    return somme
