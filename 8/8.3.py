def sorted_rands(n):
    liste = [-1,2]
    for i in range (n):
        new = random()
        longueur = len(liste)
        count = 0
        while len(liste) == longueur:
            if new < liste[count]:
                liste.insert(count, new)
                print("ok")
            count  +=1
    liste.pop(0)
    liste.pop(len(liste)-1)
    return liste
