import cv2
import numpy as np
import matplotlib.pyplot as plt


class GridMaker():

    def __init__(_self, pathToImg:str, resize=1):
        _self.resize = resize
        _self.ox, _self.oy = _self.makeGrid(pathToImg)

    def makeGrid(_self, pathToImg:str):
        # Imagen a tratar
        img = cv2.imread(pathToImg)

        # convertir la imagen a escala de grises
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Redimensionar la imagen
        width, height = img.shape[0], img.shape[1]
        dim = (int(height / _self.resize), int(width / _self.resize))
        
        # Cambia la resolución de la imagen
        img = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)

        # convertir la imagen a blanco y negro. 
        _, _self.img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

        # Mapa
        ox, oy = [], []
        for i, row in enumerate(_self.img):
            for j in range(len(row)):
                if (_self.img[i][j] == 0):
                        ox.append(j)
                        oy.append(i)
        return ox, oy

    def showMap(_self):
        # Muestra el mapa
        plt.imshow(_self.img, cmap='gray')
        plt.axis("equal")
        plt.show()


if __name__ == "__main__":
    gridMaker = GridMaker('Mazes/a.png')
    gridMaker.showMap()
    print(gridMaker.img.shape)