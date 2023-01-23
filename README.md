# Sobre el repositorio
Este repositorio acoge un trabajo para la asignatura Robots Autónomos del Máster Universitario en Inteligencia Artificial de la UPM. El objetivo de la práctica es probar distintos algoritmos de planificación de rutas en distintos mapas 2D.

# Path Planning
El problema de Path Planning consiste en encontrar un camino seguro y eficiente entre dos puntos en un entorno dado para un sistema autónomo, como un robot o un vehículo autónomo. Este problema implica tanto la planificación de la trayectoria como la evasión de obstáculos y la evitación de colisiones. El Path Planning puede ser muy complejo y requiere una combinación de algoritmos de búsqueda y evitación de obstáculos para encontrar una solución óptima.
En este trabajo se comparan distintos algorimos de planificación y búsqueda de caminos óptimos sobre mapas bidimensionales. Para ello, se utilizan varios de los algoritmos ya implementados en el repositorio https://github.com/AtsushiSakai/PythonRobotics.

# GridMaker
La clase GridMaker ubicada en el archivo GridManager se encarga de convertir una imagen de entrada en un mapa de obstáculos de dos dimensiones al cual se le puede aplicar un factor de escala para redimensionarlos. Esta clase permite crear mapas de obstáculos a partir de imágenes, lo que facilita la creación de nuevos entornos para probar los algoritmos.
