Les mises possibles et les retours correspondants quand le pari est gagn� sont donn�s ci-dessous
Mise	retour si gagn�
Num�ro exact (0 � 12)	12 fois la mise	
Pair ou Impair	2 fois la mise
Rouge ou Noir	2 fois la mise
Pour simplifier, on suppose que le z�ro est ni rouge ni noir, mais est pair.
�crire un programme qui lit ce que mise le joueur parmi :
0, 1, ..., 12
13 pour "Pair"
14 pour "Impair"
15 pour "Rouge"
16 pour "Noir"
et qui, apr�s avoir actionn� la roulette avec la commande x = roulette() o� x re�oit le nombre entre 0 et 12 tir� par la roulette, imprime le retour correspondant: 0 si le pari est perdu, ou la valeur indiqu�e si la pari est gagn�. Par exemple si la pari est 14 ("Impair") et que 7 est sorti par la roulette, le r�sultat est : 2
Votre code � tester par upylab ne doit pas avoir de param�tre dans l'input. Exemple: a = input() plut�t que a = input("Quel pari faites-vous ? : "))
Pour tester votre code, vous devez remplacer x = roulette() par x = int(input()) pour entrer ce que la roulette a tir�. Les deux premi�res lignes du code sont donc :
a = int(input()) # pari du joueur entre 0 et 16

x = int(input()) # tirage entre 0 et 12