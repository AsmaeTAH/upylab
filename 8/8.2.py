def sort_words(data):
    longueur = len(data)
    for i in range(longueur):
        j = i+1
        for j in range(longueur-1):
            if len(data[i]) > len(data[j]):
                data[i],data[j] = data[j],data[i]
            elif len(data[i]) == len(data[j]):
                if data[i] < data[j]:
                    data[i],data[j] = data[j],data[i]
    return data
