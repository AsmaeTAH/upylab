
def make_dico_list(file_dir):
    """
    cette fonction recoit le fichier de dictionnaire des mots et rend une liste de sets classes par longueur (le set a l'indice 0 est celui des mots de longueur 2)

    """
    file = open(file_dir, 'r')
    liste_mots = []
    resultat = []
    for line in file:
        line = line.rstrip()
        liste_mots.append(line)
    liste_mots.sort(key = len)
    count = 1
    s_ajouter = []
    for i in liste_mots:
        if len(i) == count:
            s_ajouter.append(i)
        else:
            if len(s_ajouter) != 0:
                resultat.append(set(s_ajouter))
            s_ajouter.clear()
            count+=1
            s_ajouter.append(i)
    resultat.append(set(s_ajouter))
    file.close()
    return resultat
