import sys, itertools
from copy import deepcopy


def main( args ):
    with open( args[1], 'r' ) as f:
        l = [line.strip().split('->') for line in f ]
        d = {}
        #leaves = []
        for entry in l:
            key, weight =entry[0].split()[0], int(entry[0].split()[1].strip('()'))
            if len(entry) > 1:
                dependencies = set(entry[1].strip().split(', '))
                #leaves.append(entry[1].strip().split(', '))
            else:
                dependencies = None
            d[key] = [weight,dependencies]
        #leaves = [c for a in leaves for c in a]
        leaves = [c for value in d.values() if value[1] != None for c in value[1]]

        for key in d.keys():
            if key not in leaves:
                print(f'bottom reached with {key}.')



if __name__ == '__main__':
    sys.exit( main( sys.argv ) )