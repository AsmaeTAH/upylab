Enonc�
Il est demand� d'additionner des valeurs naturelles lues sur input et d'imprimer le r�sultat.
La premi�re donn�e lue ne fait pas partie des valeurs � sommer. Elle d�termine si la liste contient un nombre d�termin� � l'avance de valeurs � lire ou non.
si cette premi�re donn�e vaut un nombre positif ou nul, ce nombre donne le nombre de valeurs � lire et � sommer
si la donn�e est n�gative, cela signifie que la liste des donn�es � lire sera termin� par un caract�re "F" signifiant que la liste est termin�e
Exemple 1: les donn�es lues suivantes:
4
1
3
5
7
indiquent qu'il y a 4 donn�es � sommer : 1 + 3 + 5 + 7. 
Le r�sultat � imprimer vaudra donc 16
Exemple 2: les donn�es lues suivantes:
-1
1
3
5
7
21
F
indiquent qu'il faut sommer : 1 + 3 + 5 + 7 + 21. Le r�sultat � imprimer vaudra donc 37.
Exemple 3: La donn�e
0
indique qu'il faut sommer 0 nombre. Le r�sultat � imprimer vaudra donc 0.
Conseils:
Dans la cas o� la liste est termin�e par le caract�re 'F', vous pouvez d'une part faire l'input (ex : data = input()), ensuite tester si data == 'F' et sinon additionner la valeur int(data) � ce qui a d�j� �t� somm�;
Utilisez un for dans le cas o� le nombre de valeurs � sommer est connu, un while dans le cas contraire.
Consignes:
Ne mettez pas de param�tre texte dans les input: data = input() et pas data = input("Donn�e suivante :")) par exemple;
Le r�sultat doit juste faire l'objet d'un print(res) sans texte suppl�mentaire (pas de print("r�sultat =", res) par exemple).