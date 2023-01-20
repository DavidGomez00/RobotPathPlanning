import AStar


def main():
    '''Prueba los distintos algoritmos de 
    ejecución para los distintos mapas.'''

    times = []

    for i in range(4):
        times.append(AStar.start(i + 1))

    print(times)


if __name__ == "__main__":
    main()