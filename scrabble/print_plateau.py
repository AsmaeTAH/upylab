import glob
def print_plateau():
    """cette fonction sert a imprimerle plateau ligne par ligne et ecrire leur lignes et colonnes au dessus, le jeu se jouant a partir de 1 et non de 0 alors le compte commence par 1"""
    colonnes = []
    for i in range(len(glob.plateau[1])):
        colonnes.append(str(i+1))
    print(colonnes)
    count = 1
    for i in glob.plateau:
        print(str(i)+str("  ")+str([count]))
        count +=1
