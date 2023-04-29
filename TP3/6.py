
#1. Recherche séquentielle

#a) La complexité dans le meilleur cas est O(1) si l'élément recherché est à la première position du tableau.
#b) La complexité dans le pire des cas est O(n) si l'élément recherché est à la dernière position du tableau ou s'il n'est pas présent dans le tableau.
#c) La complexité en moyenne est O(n/2).

#2. Recherche dichotomique

def dicho(liste_triee, k):
    if not liste_triee:  # cas liste vide
        return -1
    gauche, droite = 0, len(liste_triee) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste_triee[milieu] == k:
            return milieu
        elif liste_triee[milieu] < k:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1

