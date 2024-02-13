# MapleBot-Robot
Notre projet est de créer une carte d’une salle en 2D et en 3D (si les limites hardware des senseurs nous le permettent) à l’aide de senseurs montés sur un robot autonome. Une fois capable de créer la carte, nous voulons implémenter un générateur de trajectoire pour que quelconque utilisateur puisse définir sur la carte un point d’arrivé et le robot puisse s’y rendre en évitant les obstacles pré-identifié sur la carte ainsi que les objets non pré-identifié si nous avons le temps.

Environnement : Système d’exploitation (Windows version), environnement de développement, logiciels, etc.

Pour construire et contrôler le robot, nous allons utiliser un kit Lego Mindstorm EV3. Le code de contrôle pour le robot va être codé en Micropython. (https://pybricks.com/ev3-micropython/)

Pour créer une map à partir des données, on va utiliser matplotlib une librairie de Python pour analyser du data et générer des maps à partir de cette data. (https://matplotlib.org/).

Pour la génération de trajectoire, on pourrait le faire nous même (les algorithmes) en s’inspirant ou utilisant des librairies déjà existantes.
