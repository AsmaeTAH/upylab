On peut calculer approximativement le sinus de x (voir d�finition du sinus) en effectuant la sommation des n premiers termes de la s�rie (c'est-�-dire la somme infinie) :
sin(x)=x-(x3^/3!)+(x^5/5!)-(x^7/7!)+...
o� x est exprim� en radians. R��crivez cette somme sous la forme :
sin(x)=somme f(i,x) avec i allant de 0 � l'infini
On vous demande donc de trouver f(i,x). �crivez ensuite le code calculant de cette mani�re la valeur de sin(x) o� x est lu sur input. Continuez l'addition des termes successifs dans la s�rie jusqu'� ce que la valeur d'un terme devienne inf�rieure (en valeur absolue) � une constante e (prenez e=10^-6). Affichez ensuite l'approximation ainsi obtenue � l'�cran.