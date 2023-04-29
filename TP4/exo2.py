# Q1. = O(nlog(n))

# Q2.

# Q3.
def tri_fusion(liste):
    if len(liste) > 1:
        milieu = len(liste) // 2
        gauche = liste[:milieu]
        droite = liste[milieu:]
        tri_fusion(gauche)
        tri_fusion(droite)
        i = 0
        j = 0
        k = 0
        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                liste[k] = gauche[i]
                i += 1
            else:
                liste[k] = droite[j]
                j += 1
            k += 1
        while i < len(gauche):
            liste[k] = gauche[i]
            i += 1
            k += 1
        while j < len(droite):
            liste[k] = droite[j]
            j += 1
            k += 1
    return liste

if __name__ == "__main__":
    a = [10,4,5,2,3,6,1]

    print(tri_fusion(a))