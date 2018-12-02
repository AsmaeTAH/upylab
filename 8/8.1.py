    s = [5,9,1,2,7,0]
    longueur = len(s)
    for i in range(longueur):
        j = i+1
        for j in range(longueur-1):
            if s[i] < s[j]:
                s[i],s[j] = s[j],s[i]
print(alist)
