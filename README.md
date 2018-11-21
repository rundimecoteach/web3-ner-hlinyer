Geoffrey Mignonneau /
Linyer Hector /
Marceau Alexis

# Récupération des auteurs et de leurs oeuvres


### Récupération des données

Nous avons choisi de récupérer des auteurs anglais, ainsi que leurs oeuvres, à partir de biographies récupérées sur biography.org. La méthode que nous avons utilisé doit permettre une généralisation à d'autres biographies pour des auteurs d'autres formats uniques (thèses,...).


La recherche de notre programme couvrera une liste d'URL, spécifiée dans le fichier sourceFile.txt.

Afin de charger les pages web, nous avons utilisé la bibliothèque requests, qui va nous permettre de passer de liens web à une chaine de caractères.

Afin de ne conserver que le texte des pages dans lesquelles nous allons effectuer notre recherche, nous utilisons l'outil jusText, qui ne va conserver que le contenu principal de notre page et en retirer les balises html.




### Tri des éléments

Nous allons isoler les éléments en fonction de leur catégorie ("ent_type_"), conformément à un langage Spacy (langage utilisé : "en_core_web_sm").

Nous nous intéressons à deux de ces catégories :
- Person : Noms des personnes,
- Work of art : Noms des oeuvres.


Nous allons conserver tous les noms d'oeuvres, mais nous ne nous intéressons qu'à l'auteur et pas aux autres personnes. Le site biography.org nous permettrait de toujours récupérer le premier nom (qui est celui de l'auteur), mais afin de généraliser notre solution à d'autres sites biographiques, nous avons choisi de mettre en place une pondération sur le nom.

Nous stockons le nombre de fois où chaque nom est apparu, les noms apparaissant le plus fréquemment étant plus susceptibles d'appartenir à l'auteur.
Comme les noms aparaissent sous forme de mots individuels, nous retournons la liste des premiers noms, que l'humain peut ensuite traiter.

Si nous devions aller plus loin dans ce projet, il serait possible d'améliorer ce traitement en complétant les noms des personnes (voir plus bas la complétion des entités), et en recherchant si plusieurs noms sont des parties de l'un d'entre eux, puis en faisant la somme de leur pondération individuelle.




### Complétion des entités

Le tri des éléments ne nous permet de récupérer que des mots, nous devons donc rassembler les noms des personnes et oeuvres en un seul élément. Pour cela, nous allons nous intéresser à leur position dans une entité (IOB).

- Les mots en début d'entité (B) sont ajoutées à la liste d'entités.
- Les mots à l'interieur d'une entité (I) viennent compléter l'entité précédemment commencée.
- Les mots n'appartenant pas à une entité (O) n'ont pas été jugés utiles à conserver.


Les entités récupérées seront finalement sauvegardées dans le fichier results.txt.




### Observations et conclusion

Après exécution de notre programe sur un groupe d'URL, nous observons des résultats mitigés, ceux-ci nous permettant effectivement de déterminer l'auteur dans la liste de ceux proposés, et de récupérer une partie des oeuvres de l'auteur.

On remarque cependant que de nombreuses oeuvres ne sont pas repérées comme tel par le langage que nous avons utilisé avec Spacy. De plus, certains noms d'oeuvres n'apparaissent pas complets (il manque le début ou la fin), car l'entité a mal été détectée. Il peut également arriver que certains éléments, comme les "nicknames", soient détectées comme des oeuvres.

Le tri que nous avons effectué permet donc de récupérer une partie des oeuvres pour chaque auteur, en assurant la justesse maximale de nos résultats trouvés, tentant ainsi de réduire au mieux l'intervention humains après notre traitement. Au contraire, ce traitement ne conviendra pas à une recherche nécessitant de récupérer un maximum d'oeuvres, quitte à nécessiter une plus lourde intervention humaine.


Pour tester la fonctionnalité de notre programme avec d'autres sites, nous avons ajouté à nos URL un lien vers une page Wikipédia. Les résultats comportent du bruit, notamment dû aux références en fin de page (menant vers des oeuvres extérieures à l'auteur), mais gardent une cohérence. Il faudrait éliminer cette partie références pour obtenir des résultats optimaux.







