La suite de Fibonacci commence ainsi :
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,...
Ses deux premiers termes sont 0 et 1, et ensuite, chaque terme successif est la somme des deux termes pr�c�dents. Ainsi
0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8, etc.
Ecrivez un programme qui lit avec n = int(input()) une valeur n donn�e (n sup�rieure ou �gal � 2) et imprime sur une ligne, la partie de la suite de Fibonacci avec les nombres inf�rieurs ou �gaux � n, en mettant un espace apr�s chaque nombre et une fin de ligne � la fin.
Conseil: utilisez le param�tre end du print :
print(x, end = " ")
ainsi que le print qui imprime juste une fin de ligne :
print()