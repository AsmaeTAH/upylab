def verif_mot(mot,dico):
    """Cette fonction renvoie True si le mot a placer est bien un mot du dictionnaire.
    False sinon.
    Arguments :
    - mot (str): une chaine de caracteres en majuscule qui indique le mot a placer
    - dico (list) : une liste dont chaque element d'indice i, est un set de mots du dictionnaire de
    longueur (i+1). Par exemple, dico[3] pointe vers un set de tous les mots a 4 lettres.
    Valeurs de retour :
    - bool (True ou False)"""
    long_set = len(mot)
    reponse = False
    if len(dico) >= long_set:
        reponse = mot in dico[long_set-2]
    return reponse
