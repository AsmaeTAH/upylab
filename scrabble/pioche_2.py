from random import randint
def pioche_2(pioches_dispo, lettres_joueur):
    """cette fonction sert a remplir le chevalet jusqu'a avoir 7 lettres"""
    if len(pioches_dispo) > 7-len(lettres_joueur):
        for i in range(7-len(lettres_joueur)):
            id = randint(0, len(pioches_dispo)-1)
            lettre_add = pioches_dispo[id]
            lettres_joueur.append(lettre_add)
            pioches_dispo.pop(id)
    else:
        pioches_dispo = []
