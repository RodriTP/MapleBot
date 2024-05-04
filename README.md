# MapleBot-Robot
Projet de fin de parcours collégial dont le but est de créer une carte d’une salle en 2D à l’aide de senseurs montés sur un robot autonome. Une fois capables de créer la carte, nous voulons implémenter un générateur de trajectoire pour qu'un utilisateur quelconque puisse définir sur la carte un point d’arrivée et le robot puisse s’y rendre en évitant les obstacles préidentifiés sur la carte ainsi que les objets non préidentifiés si nous avons le temps.

Environnement : Système d’exploitation (version Windows), Visual Studio Code.

Pour construire et contrôler le robot, nous allons utiliser un kit Lego Mindstorm EV3. Le code de contrôle pour le robot va être codé en Micropython. (https://pybricks.com/ev3-micropython/)

Pour créer une map à partir des données, on va utiliser matplotlib une librairie de Python pour analyser des données et générer une map qui se met à jour au fur et à mesure que le robot explore l'environnement. (https://matplotlib.org/)
