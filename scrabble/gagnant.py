def gagnant(joueurs):
    """cette fonction sert a decider de qui est le gagnant en comparant les scores"""
    liste_score = []
    biggest = 0
    for i in joueurs:
        liste_score.append(i[3])
        if i[3] > biggest:
            biggest = i[3]
    id = liste_score.index(biggest)
    return id
