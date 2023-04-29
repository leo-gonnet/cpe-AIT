class Noeud():
    def __init__(self, valeur) -> None:
        self.valeur = valeur
        self.suivant = None

class ListeChainee():
    def __init__(self) -> None:
        self.tete = None
        self.queue = None
        #self.taille = 

    def inserer(self, valeur, k=None):
        nouveau_noeud = Noeud(valeur)
        if self.tete is None:
            self.tete = nouveau_noeud
            self.queue = nouveau_noeud
            return
        if k is None:
            self.queue.suivant = nouveau_noeud
            self.queue = nouveau_noeud
            return
        if k == 0:
            nouveau_noeud.suivant = self.tete
            self.tete = nouveau_noeud
            return
        noeud = self.tete
        for i in range(k-1):
            noeud = noeud.suivant
            if noeud is None:
                return
        nouveau_noeud.suivant = noeud.suivant
        noeud.suivant = nouveau_noeud
        if nouveau_noeud.suivant is None:
            self.queue = nouveau_noeud

    def supprimer(self, k):
        if self.tete is None:
            return
        if k == 0:
            self.tete = self.tete.suivant
            if self.tete is None:
                self.queue = None
            return
        noeud = self.tete
        for i in range(k-1):
            noeud = noeud.suivant
            if noeud is None:
                return
        noeud.suivant = noeud.suivant.suivant
        if noeud.suivant is None:
            self.queue = noeud

    def rechercher(self, valeur):
        noeud = self.tete
        while noeud is not None:
            if noeud.valeur == valeur:
                return True
            noeud = noeud.suivant
        return False
    
    def taile(self):
        noeud = self.tete
        taille = 0
        while noeud is not None:
            taille += 1
            noeud = noeud.suivant
        return taille

    def estVide(self):
        return self.tete is None
    
    def afficher(self):
        noeud = self.tete
        while noeud is not None:
            print(noeud.valeur)
            noeud = noeud.suivant
