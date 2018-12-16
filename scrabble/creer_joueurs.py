from random import randint

def creer_joueurs(pioches_dispo):
    """cette fonction sert a creer les differents joueurs pour le multijouers et cree leur chevalet
        elle renvoit une liste de sous listes composes de l'identifiant du joueur, son nom, son chevalet et son score

    """
    liste_joueurs = []
    lettres = []
    n_joueurs = 0
    while not 2<=n_joueurs<=4:
        try:
            nombre = input("indiquez le nombre de joueurs (2-4): ")
            nombre = int(nombre)
            n_joueurs = nombre
        except ValueError:
            print ("veuillez entrer un nombre valide")
            continue
    for i in range(n_joueurs):
        nom = str(input("veuillez entrer le nom du joueur n°" + str(i+1) + ": "))
        for l in range(7):
            id = randint(0, len(pioches_dispo)-1)
            lettre_add = pioches_dispo[id]
            lettres.append(lettre_add)
            pioches_dispo.pop(id)
        liste_joueurs.append([i+1,str(nom),list(lettres),0])
        lettres.clear()
    return(liste_joueurs)
