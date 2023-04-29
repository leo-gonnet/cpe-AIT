from random import randint
import matplotlib.pyplot as plt
from time import time
import numpy as np

from exo1 import tri_selection
from exo2 import tri_fusion
from exo3 import tri_rapide

def tabAlea(k,n=100):
    l = []
    for i in range(k):
        l.append(randint(0,n))
    return l

def main():
    index = 0
    temps_calcul_fusion = [0]
    temps_calcul_rapide = [0]
    temps_calcul_selection = [0]

    while temps_calcul_selection[-1] < 5 and index<15:
        index += 1
        tab = tabAlea(2**(index))
        t0 = time()
        tri_rapide(tab)
        t1 = time()
        tri_fusion(tab)
        t2 = time()
        tri_selection(tab)
        t3 = time()

        temps_exe_rap = t1-t0
        temps_exe_fus = t2-t1
        temps_exe_sel = t3-t2
        temps_calcul_fusion.append(temps_exe_fus)
        temps_calcul_rapide.append(temps_exe_rap)
        temps_calcul_selection.append(temps_exe_sel)

        print(f'\r',end='')
        print(f'itérations : {index}, temps fus : {temps_exe_fus}, temps rap : {temps_exe_rap}, temps sel : {temps_exe_sel}',end='')
    print('\n')


    fig = plt.figure()

    plt.yscale('log')

    plt.plot(temps_calcul_fusion, label='tri fusion')
    plt.plot(temps_calcul_rapide, label='tri rapide')
    plt.plot(temps_calcul_selection, label='tri selection')

    fig.legend()

    plt.show()

if __name__ == "__main__":
    main()