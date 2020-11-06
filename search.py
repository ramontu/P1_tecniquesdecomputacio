#Ramon Trilla Urteaga

from labyrinth import Labyrinth


def DFS(lab: Labyrinth):
    print('Starting DFS')
    trail = []
    ja_cercats = []

    start = lab.getStartCell()


    def busqueda(ultima_pos):
        """S'encarrega de buscar el camí, li ha d'entrar una posició del fill de la ultima posició del trail
            Busca si existeixen fills de la ultima posició, comprova que no s'hagin consultat abans
            i si no ha passat per alla abans o no es una posició sense sortida escull un. Si detecta que cap
            fill es viable, marca la última posició com a ja_buscda, per a vetar que intenti passar per alla
            de nou
        """
        children = ultima_pos.getChildren()     #obtenim els children de la posició d'entrada
        trail.append(ultima_pos)    #afegim la posició d'entrada al trail

        a_eliminar = []     #degut a que eliminarem posicions de childrem, creem aquest array per a guardar
                            #les posicions que eliminarem

        # recorrem totes les posicions de children per a guardar a a_eliminar les que siguin punts morts
        # o per les que ja esta passant el trail (que ens porten a un punt mort)
        for a in children:
            if ja_cercats.__contains__(a) or trail.__contains__(a):
                a_eliminar.append(a)
            elif a == lab.getEndCell():
                trail.append(a)
                return trail

        # Elimina tots els children que abans hem marcat per a eliminar
        # evita que al for de children no revisi la ultima posició si es fa algun remove
        for c in a_eliminar:
            children.remove(c)

        # Detecta si el cami es viable (te alguna posició per on seguir) no fills = children.len == 0
        # Si el cami no es viable, afegeix la ultima posició com a punt mort, neteja trail i torna a començar
        # des del principi
        # en cas contrari, mira si
        if children.__len__() == 0:
            ja_cercats.append(ultima_pos)
            trail.clear()
            busqueda(start)
        else:
            busqueda(children[0])
            #if not children[0] == lab.getEndCell():

            #else:
                #return trail

    busqueda(start) #iniciamos la iteracion
    #busqueda en profundidad (elije una rama i va hasta abajo) recursiva

    return trail


def BFS(lab: Labyrinth):
    print('Starting BFS')

    #Posteriorment afegirem a trails la posició d'inici, per aixó l'afegim aqui
    ja_buscats = [lab.getStartCell()]

    # Donat que en el BFS busquem tots els camins possibles fins que trobem el més curt,
    # necessitem varis trails. La iniciem amb la posició de sortida per a no fer saltar la verificacio de
    # camins possibles

    trails = [[lab.getStartCell()]]
    while True:     #Comencem la iteració
        # En el cas que la longitud de trails sigui 0, implicaria que no hi hauria cap camí possible
        if trails.__len__() == 0:
            print("Error al buscar un camí, es possible que no hi hagi solució?")
            break
        else:
            for j in trails:
                pos_val = j[j.__len__() - 1]
                children = pos_val.getChildren()
                if children.__len__() == 0:
                    trails.remove(j)
                else:
                    for k in children:
                        if not ja_buscats.__contains__(k):
                            prov = j.copy()
                            prov.append(k)
                            trails.append(prov)
                            if k == lab.getEndCell():
                                prov_f =trails[trails.__len__()-1]
                                return prov_f
                            ja_buscats.append(k)
                    trails.remove(j)

    # Exploracion por niveles iterativa, empezar des de la salida,
    # para la salida obtenemos getchildren() donde obtenemos los hijos del nodo

    return trails


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
