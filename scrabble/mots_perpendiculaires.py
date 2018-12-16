def mots_perpendiculaires(coup,plateau,dico):
    """
Lorsqu'un mot est place sur le plateau de jeu, il est
possible qu'il soit adjacent a des lettres deja
presentes sur le plateau. De nouveaux mots perpendiculaires
au mot a placer sont alors formes.
3 cas sont possibles:
- Si aucun mot perpendiculaire n'est forme, cette fonction
renvoie une liste contenant un element : le mot a placer.
- S'il existe des mots perpendiculaires et qu'ils appartiennet
TOUS au dictionnaire, cette fonction renvoie la liste contenant tous
les nouveaux mots formes (le mot a placer et les nouveaux mots
perpendiculaires), tries dans l'ordre alphabetique.
- S'il existe des mots perpendiculaires et qu'au moins un d'entre
eux n'existe pas dans le dictionnaire, la fonction renvoie une
liste vide [].
On considere que le mot a placer respecte bien les bornes du plateau et
qu'il n'y a pas de conflit entre les lettres que le joueur veut placer
sur le plateau et les lettres existantes, aux positions qui seront
utilisees pour ces lettres. Autrement dit, pour chaque lettre a placer,
soit la case est vide, soit la lettre a placer est deja presente.
Ceci n'est pas a tester dans la fonction, mais c'est un pre-requis a
son utilisation.
-Arguments:
- coup (tuple): un tuple a 3 elements:
- mot (str): une chaine de caractere en majuscule qui indique le mot a placer
- pos (tuple) : un tuple d'entiers (l,c) qui indiquent le numero de ligne (l),
et le numero de la colonne (c) de la premiere lettre du mot a placer
- dir (str) : un charactere ("h" ou "v") qui indique la direction du mot
- plateau (liste) : une liste de 15 sous-listes
qui representent chacune une ligne du plateau
de jeu. Elles contiennent chacune, soit un
underscore pour indiquer que la case est vide,
soit une lettre si elle a deja ete placee la
auparavant.
- dico (list) : une liste dont chaque element d'indice i, est un set de mots du dictionnaire de
longueur (i+1). Par exemple, dico[3] pointe vers un set de tous les mots a 4 lettres.
- Valeurs de retour:
- liste de chaine de caracteres
"""

    mot, pos ,direction = coup
    l,c = pos
    count = 0
    count_mot = 0
    m_ajouter =""
    liste_mots =[]
    dimensions = (len(plateau),len(plateau[0]))
    if direction == 'h':
        for i in mot:
            count_mot = 0
            m_ajouter= ""
            if plateau[l][c+count] == "_":
                if l != 0:
                    if plateau[l+1][c+count] != "_" or plateau[l-1][c+count] != "_":
                        count_mot-=1
                        while plateau[l+count_mot][c+count] != "_" and l+count_mot != 0:
                            count_mot -=1
                        count_mot+=1
                        while plateau[l+count_mot][c+count] != "_" or count_mot == 0 :
                            if (plateau[l+count_mot][c+count] != "_"):
                                m_ajouter += plateau[l+count_mot][c+count]
                            else: m_ajouter += i
                            count_mot +=1
                else:
                    if plateau[l+1][c+count] != "_":
                        while plateau[l+count_mot][c+count] != "_" or l+count_mot != dimensions[0]:
                            if plateau[l+count_mot][c+count] != "_":
                                m_ajouter += plateau[l+count_mot][c+count]
                                count_mot +=1
                if m_ajouter != "":
                    liste_mots.append(str(m_ajouter))
            count+=1
    else:
        for i in mot:
            count_mot = 0
            m_ajouter= ""
            if plateau[l+count][c] == "_":
                if c != 0:
                    if plateau[l+count][c+1] != "_" or plateau[l+count][c-1] != "_":
                        count_mot-=1
                        while plateau[l+count][c+count_mot] != "_" and l+count != 0:
                            count_mot -=1
                        count_mot+=1
                        while plateau[l+count][c+count_mot] != "_" or count_mot == 0 :
                            if (plateau[l+count][c+count_mot] != "_"):
                                m_ajouter += plateau[l+count][c+count_mot]
                            else:
                                m_ajouter += i
                            count_mot +=1
                else:
                    if plateau[l+count][c+1] != "_":
                        while plateau[l+count][c+count_mot] != "_" or l+count != dimensions[0]:
                            if plateau[l+count][c+count_mot] != "_":
                                m_ajouter += plateau[l+count][c+count_mot]
                                count_mot +=1
                if m_ajouter != "":
                    liste_mots.append(str(m_ajouter))
            count+=1
    fautes = 0
    for i in liste_mots:
        if not verif_mot(i, dico):
            fautes +=1
    if fautes ==0:
        liste_mots.append(mot)
        liste_mots.sort()
    else:
        liste_mots =[]
    return liste_mots
