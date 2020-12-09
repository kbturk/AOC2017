import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def tot_weight(key: str, d: Dict[str, Tuple[int, Set[str]]]) -> int:
    child_weight = [ tot_weight(item,d) for item in d[key][1] ]
    #print(child_weight)
    if len(set(child_weight)) > 1:
        print(f"issue found. {key}'s children {d[key][1]} have different weights: {child_weight}. one of these is off")
        l = list(zip(d[key][1], child_weight))
        for i in range(len(child_weight)):
            if l[i][1] == l[i+1][1]:
                continue
            elif l[i][1] == l[i+2][1]:
                continue
            else:
                diff = - abs(l[i][1] - l[i-1][1])
                name, off = l[i]
                print(f'{name} is off by {diff}, weight should be: {d[name][0]+ diff}')
                break
    mass_weight = d[key][0] + sum(child_weight)
    return mass_weight

def main(args: List[str]) -> int:
    with open( args[1], 'r' ) as f:
        l = [line.strip().split('->') for line in f ]
        d: Dict[str, Tuple[int, Set[str]]] = {}
        #part1:
        for entry in l:
            key, weight =entry[0].split()[0], int(entry[0].split()[1].strip('()'))
            if len(entry) > 1:
                dependencies = set(entry[1].strip().split(', '))
            else:
                dependencies = set()
            d[key] = (weight,dependencies)
        leaves = [c for value in d.values() for c in value[1]]
        for key in d.keys():
            if key not in leaves:
                bottom = key
                print(f'bottom reached with {bottom}.')

        #part2:
        #print(d)
        tot_weight(bottom,d)

    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )