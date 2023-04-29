def maxliste(liste):
    if len(liste) == 0:
        return None
    if len(liste) == 1:
        return liste[0]
    a = liste[:len(liste)//2]
    b = liste[len(liste)//2:]
    return max(maxliste(a), maxliste(b))

print(maxliste([1,3]))