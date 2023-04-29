import random as rd

sa = [1,2,3,4,5,6,7,8,9,10]

parent1 = rd.sample(sa, len(sa))

parent2 = rd.sample(sa, len(sa))

nb_villes = len(parent1)

enfant = [None] *   nb_villes
gene_debut, gene_fin = sorted([rd.randint(0, nb_villes) for _ in range(2)])
gene_debut, gene_fin = 3,7

villes_p1 = parent1[gene_debut:gene_fin]
villes_p2 = [v for v in parent2 if v not in villes_p1]

enfant[gene_debut:gene_fin] = villes_p1
print(enfant)

for i in range(gene_fin, nb_villes):
    if enfant[i] == None:
        enfant[i] = villes_p2.pop(0)
for i in range(0, gene_debut):
    if enfant[i] == None:
        enfant[i] = villes_p2.pop(0)

print(parent1)
print(parent2)
print(enfant)