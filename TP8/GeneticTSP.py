import os
import math
import random as rd
import csv
import GeneticTSPGui
import time
import matplotlib.pyplot as plt

class PVC_Genetique:
    def __init__(self, liste_villes, taille_pop=40, nb_generations=100, elitisme=0.5, croisement=0.6, mutation=0.3):
        self.afficher = True
        self.gui = GeneticTSPGui.PVC_Genetique_GUI(liste_villes)

        self.liste_villes = liste_villes
        self.taille_pop = taille_pop
        self.population = Population()
        self.nb_villes = len(liste_villes)

        self.nb_generations = nb_generations
        self.elitisme = elitisme
        self.mutation = mutation
        self.croisement = croisement

        self.meilleur_trajet = Trajet(liste_villes)
        self.meilleurs_trajets = []

    @staticmethod # pour le debug
    def croiser(parent1, parent2):
        nb_villes = len(parent1.villes)

        enfant = [None] * nb_villes

        gene_debut, gene_fin = sorted([rd.randint(0, nb_villes) for _ in range(2)])

        villes_p1 = parent1.villes[gene_debut:gene_fin]
        villes_p2 = [v for v in parent2.villes if v not in villes_p1]

        enfant[gene_debut:gene_fin] = villes_p1

        for i in range(gene_fin, nb_villes):
            if enfant[i] == None:
                enfant[i] = villes_p2.pop(0)
        for i in range(0, gene_debut):
            if enfant[i] == None:
                enfant[i] = villes_p2.pop(0)
        
        #[print(f"{v.nom if isinstance(v, Ville) else None} ", end='') for v in enfant]
        #print('')

        trajet_enfant = Trajet(enfant)

        return trajet_enfant 
    
    def muter(self, trajet):
        if rd.random() < self.mutation:
            gene_debut, gene_fin = sorted([rd.randint(0, self.nb_villes) for _ in range(2)])

            villes = trajet.villes
            villes[gene_debut:gene_fin] = reversed(villes[gene_debut:gene_fin])
        return Trajet(trajet.villes.copy() , melange=False)
    
    def selectionner(self):
        nb_elite = math.ceil(self.taille_pop * self.elitisme)
        return self.population.meilleurs(nb_elite if nb_elite > 2 else 2)
        
    def evoluer(self):
        nouvelle_pop = Population()
        parents = self.selectionner()
        nouvelle_pop.trajets = parents.copy()

        for trajet in nouvelle_pop.trajets: # mutation
            self.muter(trajet)

        """
        nouveaute = int( (1 - self.croisement - self.mutation)*self.taille_pop )
        for _ in range(nouveaute): # nouveaute ~ mutation forte
            nouvelle_pop.ajouter(Trajet(rd.sample(parents[0].villes, self.nb_villes)))
        """
            
        while len(nouvelle_pop.trajets) < self.taille_pop: # croisement
            p1, p2 = rd.sample(parents, 2)
            enfant = self.croiser(p1, p2)
            nouvelle_pop.ajouter(enfant)
        return nouvelle_pop

    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def plot_fin(self):
        plt.plot(range(1, len(self.meilleurs_trajets) + 1), self.meilleurs_trajets)
        plt.xlabel('Génération')
        plt.ylabel('Longueur du meilleur trajet')
        plt.title('Évolution de la longueur du meilleur trajet')
        plt.show()
    
    def executer(self, attente):
        self.population.initialiser(self.taille_pop, self.liste_villes)
        for i in range(self.nb_generations):
            
            mtg = self.population.meilleurs(1)[0]
            self.meilleurs_trajets.append(mtg.longueur)
            if self.meilleur_trajet.longueur > mtg.longueur:
                self.meilleur_trajet = Trajet(mtg.villes.copy(), melange=False)

            self.population = self.evoluer()
            
            if self.afficher:
                self.gui.afficher(meilleur=self.meilleur_trajet, courant=mtg, pas=1, afficher_noms=False)
                if attente:
                    time.sleep(attente)

        self.plot_fin()
        self.gui.window.mainloop()


class Ville():
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y

    def coos(self):
        return (self.x, self.y)

    def distance_vers(self, ville):
        return math.dist(self.coos(), ville.coos())

    def  __str__(self):
        return self.nom + " (" + str(self.x) + "," + str(self.y) + ")"

class Trajet():

    def __init__(self, villes, melange=True):
        if melange:
            self.villes = rd.sample(villes, len(villes))
        else:
            self.villes = villes
        self.longueur = self.calc_longueur()

        if not self.est_valide():
            raise ValueError('Liste de villes fournie invalide')
    
    def calc_longueur(self):
        return sum([self.villes[i].distance_vers(self.villes[i+1]) for i in range(len(self.villes)-1)])
    
    def changer_villes(self, villes):
        self.villes = villes
        self.longueur = self.calc_longueur()
    
    def est_valide(self):
        noms_villes = [v.nom for v in self.villes]
        return len(set(noms_villes)) == len(noms_villes)
    
    def __str__(self):
        return ' -> '.join([v.nom for v in self.villes]) 
    
class Population():

    def __init__(self):
        self.trajets = []

    def initialiser(self, taille, liste_villes):
        self.trajets = [Trajet(liste_villes) for _ in range(taille)]
    
    def ajouter(self, trajet):
        self.trajets.append(trajet)

    def meilleurs(self, compte):
        liste_trajets = sorted(self.trajets.copy(), key=lambda t: t.longueur)
        return liste_trajets[:compte]

    def __str__(self):
        return '\n'.join([t.__str__() for t in self.trajets])

def generer_villes(nb_villes=20, x_max=300, y_max=300):
    return [v for v in [Ville(f'V{i}', rd.randint(0, x_max), rd.randint(0, y_max)) for i in range(nb_villes)]]

def lire_csv(nom_fichier):
    with open(nom_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [Ville(row[0], int(row[1]), int(row[2])) for row in reader]


def main():
    villes = lire_csv('30.csv')
    villes2 = generer_villes(15)

    """
    parent1 = Trajet(villes)
    parent2 = Trajet(villes)
    parent1.changer_villes(villes)
    parent2.changer_villes(villes)
    enfant = PVC_Genetique.croiser(parent1, parent2)
    
    print([ville.nom for ville in parent1.villes])
    print([ville.nom for ville in parent2.villes])
    print([ville.nom for ville in enfant.villes])
    """

    pvc = PVC_Genetique(villes2,
                        taille_pop=100,
                        nb_generations=1000,
                        elitisme=0.9, 
                        croisement=0.63,
                        mutation=0.1)
    
    pvc.executer(attente=None)




if __name__ == "__main__":
    main()