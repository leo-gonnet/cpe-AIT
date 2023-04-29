# Exercice 3. Réception à l’Ambassade

>a) L’Ambassadeur de France organise une visioconférence avec 48 de ses homologues ; il prétend que chaque ambassadeur connaît exactement 11 autres personnes présentes. Est-ce possible ?

Je peux vérifier si c'est possible avec le théorème des poignées de main :
**la somme des degrés des sommets dans un graphe est égale au double du nombre d'arêtes**. Autrement dit, si chaque ambassadeur connaît exactement 11 autres personnes, cela signifie que le degré de chaque sommet dans le graphe est de 11.
On doit donc avoir :
```
48 * 11 = 2 * nombre d'arêtes
```
Or le nombre d'arêtes dans un graphe complet de *n* sommets est :
```
n × (n - 1) / 2
```
 Par conséquent, le nombre d'arêtes dans le graphe en question serait 1128, qui est pair, donc c'est bien possible.


>b) L’un des invités est absent. L’affirmation de l’Ambassadeur est-elle possible dans cette nouvelle situation ?



>c) Chaque ambassadeur a salué chacun de ses homologues. Combien y a-t-il eu de salutations lors de la soirée ?