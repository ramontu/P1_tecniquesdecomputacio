#Ramon Trilla Urteaga
import sys

from labyrinth import Labyrinth


def DFS(lab: Labyrinth):
    """Fa una busqueda en profunditat (escull una rama i va fins al final), la solució esta implementada de forma recursiva
    """
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
        # si detecta que un dels children es la posició final, l'afegeix al trail i retorna el trail
        for a in children:
            if (ja_cercats.__contains__(a)) or (trail.__contains__(a)):
                a_eliminar.append(a)
            elif a == lab.getEndCell():
                trail.append(a)
                return trail

        # Elimina tots els children que abans hem marcat per a eliminar
        # evita que al for de children no revisi la ultima posició si es fa algun remove
        for c in a_eliminar:
            children.remove(c)

        # Detecta si el cami es viable (te alguna posició per on seguir) no fills => children.len == 0
        # Si el cami no es viable, afegeix la ultima posició com a punt mort i aixi no tornará a passar pel mateix lloc
        # que portaria a la fucio a arribar al mateix punt mort. Elimiminem el pas actual i l'anterior de trail
        # i iniciem la busqueda des de la posició anterior a la qu ens ha portat aqui
        if children.__len__() == 0:
            ja_cercats.append(ultima_pos)
            trail.remove(ultima_pos)    #eliminem la posició que ens porta a un punt mort del trail.
            trail.pop(trail.__len__()-1)#Degut a com esta implementat la funció, tambe hem de eliminar
                                        #de trail la posició anterior a la que ensha postat al punt mort
                                        #ja que sinó podria trobar-se en un bucle infinit
            busqueda(trail[trail.__len__()-1])
        else:
            busqueda(children[0])

    busqueda(start) #iniciem la iteració des de la posició start (aixó nomes pasará la primera vegada)


    return trail


def BFS(lab: Labyrinth):
    """
    Fa una busqueda per nivells de forma iterativa
    """
    print('Starting BFS')

    #Posteriorment afegirem a trails la posició d'inici, per aixó l'afegim aquí
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
            #comprova cada trail
            for j in trails:
                pos_val = j[j.__len__() - 1] #agafem la ultima posició de cada taril per a obtenir els seus children
                children = pos_val.getChildren() #d'aquesta manera independentment de la llargada sempre tenim els
                                                 #children de la ultima posició
                if children.__len__() == 0: #si detectem que aquell camí no te cap children, implica que s'ha acabat
                                            #per tant eliminem el camí de trails
                    trails.remove(j)
                else:
                    #per cada children que tingui el camí actual volem crear un camí nou (afegint children[n] al final)
                    # Per tant primer filtem per veure si aquest children ja ha estat buscat, sino el conté, copiem el
                    # el trail i li afegim el children k al final i l'afegim a trails. Llavors mirem si aquest children
                    # es la posició final, si ho és retornem el trail (que ja te la posició k inclosa). De no ser aixi
                    # afegim la posició com a ja buscada
                    for k in children:
                        if not ja_buscats.__contains__(k):
                            prov = j.copy()
                            prov.append(k)
                            trails.append(prov) #'aqui'
                            if k == lab.getEndCell():
                                prov_f =trails[trails.__len__()-1] #hem afegit abans 'aqui' a trails al final de tot
                                return prov_f
                            ja_buscats.append(k)
                    #borrem el trail j degut a que no te cap dels childrens i es inutil guardar-lo ja que els camins
                    # derivats d'aquest trail j ja han estat afegits a 'aqui'.
                    trails.remove(j)


    # para la salida obtenemos getchildren() donde obtenemos los hijos del nodo

    return trails


if __name__ == '__main__':
    algo_choices = ['BFS', 'DFS']
    algo_funcs = [BFS, DFS]

    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('labyrinth_file')
    argp.add_argument('algo', choices =algo_choices)

    args = argp.parse_args()
    laby = Labyrinth.load_from_file(args.labyrinth_file)
    print(laby)
    result_trail = algo_funcs[algo_choices.index(args.algo)](laby)
    if result_trail:
        print(f'{args.algo} found solution that has {len(result_trail)} steps:')
        print(result_trail)