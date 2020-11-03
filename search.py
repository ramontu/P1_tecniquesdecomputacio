from labyrinth import Labyrinth


def DFS(lab: Labyrinth):
    print('Starting DFS')
    trail = []
    ja_cercats = []
    start = lab.getStartCell()

    # TODO busqueda en profundidad (elije una rama i va hasta abajo) recursiva

    return trail


def BFS(lab: Labyrinth):
    print('Starting BFS')
    ja_buscats = [laby.getStartCell()]
    desviaciones = [[laby.getStartCell()]]
    while True:
        if desviaciones.__len__() == 0:
            print("Error al buscar un camí, es possible que no hi hagi solució?")
            break
        else:
            for j in desviaciones:
                pos_val = j[j.__len__() - 1]
                children = pos_val.getChildren()
                if children.__len__() == 0:
                    desviaciones.remove(j)
                else:
                    for k in children:
                        if not ja_buscats.__contains__(k):
                            prov = j.copy()
                            prov.append(k)
                            desviaciones.append(prov)
                            if k == laby.getEndCell():
                                prov_f =desviaciones[desviaciones.__len__()-1]
                                print(prov_f)
                                return prov_f.append(k)
                            ja_buscats.append(k)
                    desviaciones.remove(j)

    # Exploracion por niveles iterativa, empezar des de la salida,
    # para la salida obtenemos getchildren() donde obtenemos los hijos del nodo

    return desviaciones


if __name__ == '__main__':
    algo_choices = ['BFS', 'DFS']
    algo_funcs = [BFS, DFS]

    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('labyrinth_file')
    argp.add_argument('algo', choices=algo_choices)

    args = argp.parse_args()
    laby = Labyrinth.load_from_file(args.labyrinth_file)
    print(laby)
    result_trail = algo_funcs[algo_choices.index(args.algo)](laby)
    if result_trail:
        print(f'{args.algo} found solution that has {len(result_trail)} steps:')
        print(result_trail)
