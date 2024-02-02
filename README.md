# MapleBot-Robot
Notre projet à pour but de créer une carte de la classe en 2D et 3D (si les limites hardware des senseurs nous le permet) à l’aide de senseurs montés sur un robot autonome. Une fois capable de créer la map, nous voulons implémenter un générateur de trajectoire pour qu’un utilisateur définisse sur la map un point d’arrivé et le robot puisse s’y rendre en évitant les obstacles pré-identifié sur la map et les objets non pré-identifié d’avance (optionnel si on à le temps)

Environnement : Système d’exploitation (Windows version), environnement de développement, logiciels, etc.

Pour construire et contrôler le robot, nous allons utiliser un kit Lego Mindstorm EV3. Le code de contrôle pour le robot va être codé en Java avec l’API leJOS (https://lejos.sourceforge.io/ev3.php)

Pour créer une map à partir des données, on va utiliser matplotlib une librairie de Python pour analyser du data et générer des maps à partir de cette data. (https://matplotlib.org/). Pour voir le code du mapping : https://github.com/RodriTP/MapleBot-Mapping 

Pour la génération de trajectoire, on pourrait le faire nous même (les algorithmes) en s’inspirant ou utilisant des librairies déjà existantes.
