# UN TP sur le Design Applicatif

Commencer par faire l'hexagone, tout mettre dans les Use case puis au fur et à mesure du refacto mettre l'intelligence 
dans le metier

domain : c'est l'intérieur de l'hexagone, contient l'intelligence metier, n'est couplé à aucun framework, ne manipule 
que des interfaces

domain/model : Nos objets métiers, ils contiennent l'intelligence métier (comment on modifie un prix, ce qu'est un prix pour le metier,
comment on met à jour les prix des chambres de l'hôtel)

domain/repository : nos interfaces qui nous permettent d'interagir avec l'extérieur, côté server-side

domain/use_cases : notre user-side de l'hexagone côté intérieur, c'est juste un orchestrateur il n'y a dedans aucune 
intelligence (pas même de boucles ou de if!) c'est vraiment une liste ordonnée de fonctions

repository : nos implémentations concrètes des interfaces server-side

Tests : Doit-on tester chaque objet metier ou bien on ne teste que les uses cases ?
Dans nos tests on voit qu'on a défini un server-side exprès pour les tests : notre Stub
côté user-side : le script test_...uses_case est notre côté gauche de l'hexagone qui vient se brancher sur les use_cases