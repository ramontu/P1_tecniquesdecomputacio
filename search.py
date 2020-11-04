from labyrinth import Labyrinth


def DFS(lab: Labyrinth):
    print('Starting DFS')
    trail = []
    ja_cercats = []

    start = lab.getStartCell()


    def busqueda(ultima_pos):
        children = ultima_pos.getChildren()
        trail.append(ultima_pos)
        a_eliminar = []
        for a in children:
            if (ja_cercats.__contains__(a)) or (trail.__contains__(a)):
                a_eliminar.append(a)
            elif a == lab.getEndCell():
                return trail
        for c in a_eliminar:        #evita que al for de children no revisi la ultima posició si es fa algun remove
            children.remove(c)
        if children.__len__() == 0: #no te fills, per tant no te ruta
            ja_cercats.append(ultima_pos)
            trail.clear()
            busqueda(start)
        else:
            if not children[0] == lab.getEndCell():
                busqueda(children[0])
            else:
                return trail

    busqueda(start)
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
                                return prov_f
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
