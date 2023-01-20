import pandas as pd
import AStar
import dstar
import bidirectional_a_star
import breadth_first_search
import depth_first_search

def main():
    '''Prueba los distintos algoritmos de 
    ejecución para los distintos mapas.'''

    data = {
        'Algoritmo': [],
        'Mapa': [],
        'Time': [],
        'Cost': []
    }

    # Dataframe
    df = pd.DataFrame(data)
    #
    # Algorithms
    for a in ['AStar', 'BidirectionalAStar', 'DStar', 'Depth', 'Breadth']:
        for i in range(4):
            time = 0
            cost = 0
            # Ejecutamos el algoritmo correspondiente
            if (a == 'AStar'):
                time, cost = AStar.start(i+1)
            elif (a == 'BidirectionalAStar'):
                time, cost = bidirectional_a_star.start(i+1)
            elif (a == 'DStar'):
                time, cost = dstar.start(i+1)
            elif (a == 'Depth'):
                time, cost = depth_first_search.start(i+1)
            elif (a == 'Breadth'):
                time, cost = breadth_first_search.start(i+1)
            
            tmp_df = pd.DataFrame({
                'Algoritmo': a,
                'Mapa': 'maze' + str(i + 1),
                'Time': time,
                'Cost': cost
            }, index=[0])
            df = pd.concat([df, tmp_df], ignore_index=True)

    df.to_excel("Results.xlsx")


if __name__ == "__main__":
    main()