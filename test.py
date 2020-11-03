from labyrinth import Labyrinth
from search import BFS, DFS

if __name__ == '__main__':
    algo_choices = ['BFS', 'DFS']
    algo_funcs = [BFS, DFS]

    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('labyrinth_file')
    argp.add_argument('algo', choices=algo_choices)

    args = BFS
    laby = Labyrinth.load_from_file(args.labyrinth_file)
    print(laby)
    result_trail = algo_funcs[algo_choices.index(args.algo)](laby)
    if result_trail:
        print(f'{args.algo} found solution that has {len(result_trail)} steps:')
        print(result_trail)
