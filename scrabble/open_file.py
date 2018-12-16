def load_fichier_lettres(nom_fichier_lettres):
    """Cette fonction ouvre et lit un fichier texte
    dont le nom est fourni en argument.
    Ce fichier contient 26 lignes (une pour
    chaque lettre de l'alphabet). Chaque ligne
    est composee d'une lettre, d'un nombre
    d'occurences de cette lettre dans le jeu
    et des points que la lettre rapporte au
    joueur s'il la place, chacun separe par
    un espace. (cf fin de la page 2 de l'enonce
    pour voir un extrait du fichier
    (lettres.txt)).
    Elle renvoie ensuite deux dictionnaires dont
    les cles sont les lettres contenues dans le
    fichier texte et les valeurs sont respectivement
    le nombre d'occurences et les points que la lettre
    rapporte.
    Arguments :
    - nom_fichier_lettres (str) : Un chaine de caractere
    qui represente le nom du fichier texte a ouvrir
    Valeurs de retour (dans cet ordre):
    - dict : un dictionnaire avec comme cles les lettres contenues dans le fichier et
    comme valeur le nombre d'occurences de
    cette lettre
    - dict : un dictionnaire avec comme cles
    les lettres contenues dans le fichier et
    comme valeur les points associes a chaque lettre
    """
    lettres = open(nom_fichier_lettres, "r")
    dic_val = {}
    dic_occ = {}
    for ligne in lettres:
        key0 = ligne.split()[0]
        key1 = ligne.split()[1]
        key2 = ligne.split()[2]
        new_to_val = {key0: int(key1)}
        dic_val.update(new_to_val)
        new_to_occ = {key0: int(key2)}
        dic_occ.update(new_to_occ)
    lettres.close()
    return dic_val, dic_occ
