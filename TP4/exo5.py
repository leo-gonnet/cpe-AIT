import numpy as np

from exo4 import tabAlea
from exo3 import tri_rapide

def bonbon_recursif(tab, e):
#flemme de trouver une méthode moins efficace que celle qui me vient naturellement en tête
    ...

def bonbon_efficace(tab, e):
    n = len(tab)
    if n<1 or e<1 or n<e:
        return 'Erreur'
    t = tri_rapide(tab)

    min, meilleur_i = n, 0
    for i in range(n-e):
        delta = t[i+e-1] - t[i]
        if delta < min:
            min = delta
            meilleur_i = i
        if min == 0:
            break
    return(min, t[meilleur_i:meilleur_i+e])

def main():

    tab = tabAlea(10)
    b = bonbon_efficace(tab, 3)
    print(np.array(tab))
    print(b)

if __name__ == "__main__":
    main()