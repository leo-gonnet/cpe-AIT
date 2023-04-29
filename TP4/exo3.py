def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        inf = [x for x in liste[1:] if x < pivot]
        sup = [x for x in liste[1:] if x >= pivot]
        return tri_rapide(inf) + [pivot] + tri_rapide(sup)

if __name__ == "__main__":
    a = [10,4,5,2,3,6,1]
    print(tri_rapide(a))