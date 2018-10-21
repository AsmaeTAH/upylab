�crivez un mini jeu : le programme g�n�re de mani�re (pseudo-) al�atoire un nombre naturel (nombre secret) dans l'intervalle entre 0 et 100.
Ensuite, le joueur doit deviner ce nombre en utilisant le moins d'essais possible.
A chaque tour le joueur peut faire un essai et le programme doit donner une parmi les r�ponses suivantes:
"Trop grand" : Si le nombre secret est plus petit et qu'on n'est pas au maximum d'essais
"Trop petit" : Si le nombre secret est plus grand et qu'on n'est pas au maximum d'essais
"Gagn� en n essais !" : Si le nombre secret est trouv�
"Perdu ! Le secret �tait", nombre : Si vous avez fait 6 essais sans trouver le nombre secret
Le joueur a maximum 6 essais ; s'il ne devine pas le secret apr�s 6 essais, le programme s'arr�te apr�s avoir �crit "Perdu ! Le secret �tait", nombre"
Exemple d�ex�cution (apr�s la g�n�ration du nombre � deviner):
50
Trop grand
8
Trop petit
20
Trop petit
27
Gagn� en 4 essais !
Pour qu'Upylab puisse tester si votre solution est correcte, il faut que vous respectiez strictement cette s�quence. Si par exemple, vous n'affichez pas Trop petit ou Trop grand, le nombre suivant ne sera pas fourni par le syst�me et votre solution sera consid�r�e comme incorrecte
En pratique, vous devez d�buter votre code comme suit :
import random
NB_ESSAIS_MAX = 6
secret = random.randint(0,100)
et ne pas faire d'autre appel � randint ou � une autre fonction de random
Conseil pour le d�bogage de votre code: le programme test d'UpyLaB utilise l'argument entier affich� en sortie, comme seed du module random. Cela signifie qu'apr�s avoir import� random, l'instruction :
random.seed(argument)
est r�alis� par UpyLaB avant de r�aliser l'instruction :
secret = random.randint(0,100)
qui fournit le nombre � deviner.
Attention: l'argument n'est donc pas le nombre � deviner, mais bien ce qui permet au programme de le g�n�rer.

En faisant de m�me, vous pouvez r�pliquer une ex�cution test