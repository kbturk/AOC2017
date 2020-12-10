import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple


def main(args: List[str]) -> int:
    with open( args[1], 'r' ) as f:
        l = [ line.strip().split() for line in f ]

    registrar = {key: 0 for key in list( set( item[0] for item in l ) )}

    true_max = 0
    for item in l:
        reg1,act,int1,_,reg2,opr,int2 = item

        if eval(reg2+opr+int2,{},registrar):
            registrar[reg1] += (-1 if act == 'dec' else 1)*int(int1)
            true_max = max(true_max,max(registrar.values()))
    print(f'max: {max(registrar.values())}, true_max: {true_max}\n{registrar}')
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )