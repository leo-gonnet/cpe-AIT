from Exo2 import Noeud,ListeChainee

class Pile:
    def __init__(self):
        self.liste_chainee = ListeChainee()

    def empiler(self, valeur):
        self.liste_chainee.inserer(valeur)

    def depiler(self):
        if self.estVide():
            return None
        valeur = self.liste_chainee.queue.valeur
        self.liste_chainee.supprimer(valeur)
        return valeur

    def sommet(self):
        if self.estVide():
            return None
        return self.liste_chainee.tete.valeur

    def estVide(self):
        return self.liste_chainee.estVide()

    def taille(self):
        return self.liste_chainee.taille()
    
    def afficher(self):
        return self.liste_chainee.afficher()

def valider_syntaxe_fichier(path):
    fichier = open(path, "r")
    pile = Pile()
    cpt_ligne = 1
    for i, caractere in enumerate(fichier.read()):
        print(i, caractere)
        if caractere == '\n':
            cpt_ligne += 1
        elif caractere in '{[(<':
            pile.empiler(caractere)
        elif caractere in '}])>':
            ouvrant = pile.depiler()
            print("ouvrant:", ouvrant, "carac:", caractere)
            if (caractere == '}' and ouvrant != '{') or (caractere == ']' and ouvrant != '[') or (caractere == '>' and ouvrant != '<') or (caractere == ')' and ouvrant != '('):
                return f"Erreur de syntaxe à la ligne {cpt_ligne}"
    if not pile.estVide():
        return f"Erreur de syntaxe à la dernière ligne {cpt_ligne}"
    return "Aucune erreur de syntaxe"

print(valider_syntaxe_fichier("Exo3.txt"))
