import pandas as pd
import AStar
import dstar
import bidirectional_a_star

def main():
    '''Prueba los distintos algoritmos de 
    ejecución para los distintos mapas.'''

    data = {
        'Algoritmo': [],
        'Mapa': [],
        'Time': [],
        'Coste': []
    }

    # Dataframe
    df = pd.DataFrame(data)

    # Algorithms
    for a in ['AStar', 'BidirectionalAStar', 'DStar']:
        for i in range(4):
            time = 0
            # Ejecutamos el algoritmo correspondiente
            if (a == 'AStar'):
                time = AStar.start(i+1)
            elif (a == 'BidirectionalAStar'):
                time = bidirectional_a_star.start(i+1)
            elif (a == 'DStar'):
                time = dstar.start(i+1)
            
            tmp_df = pd.DataFrame({
                'Algoritmo': a,
                'Mapa': 'maze' + str(i + 1),
                'Time': time,
                'Cost': 0
            }, index=[0])
            df = pd.concat([df, tmp_df], ignore_index=True)

    pd.to_excel("Results.xlsx")


if __name__ == "__main__":
    main()