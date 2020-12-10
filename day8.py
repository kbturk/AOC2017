import sys, itertools
from copy import deepcopy

from typing import Dict, List, Optional, Set, Tuple

def action(action: str, int1: int) -> int:
    if action == "inc":
        return int1
    else:
        return -int1

def evaluate(reg2:str,opr:str,int2:int,registrar:Dict[str,int]) -> bool:
    if opr == ">":
        if registrar[reg2] > int2:
            return True
        else:
            return False

    if opr == "<":
        if registrar[reg2] < int2:
            return True
        else:
            return False

    if opr == ">=":
        if registrar[reg2] >= int2:
            return True
        else:
            return False

    if opr == "==":
        if registrar[reg2] == int2:
            return True
        else:
            return False

    if opr == "<=":
        if registrar[reg2] <= int2:
            return True
        else:
            return False
    if opr == "!=":
        if registrar[reg2] != int2:
            return True
        else:
            return False

    print(f"Nothing matched {opr}")
    return False

def main(args: List[str]) -> int:
    with open( args[1], 'r' ) as f:
        l = [ line.strip().split() for line in f ]

    registrar = {key: 0 for key in list( set( item[0] for item in l ) )}
    #print(registrar)
    true_max = 0
    for item in l:
        reg1,act,int1,_,reg2,opr,int2 = item
        #print(reg1,act,int1,reg2,opr,int2)
        #evaluate:
        if evaluate(reg2,opr,int(int2),registrar):
            registrar[reg1] += action(act,int(int1))
        if max(registrar.values()) > true_max:
            true_max = max(registrar.values())
    print(f'max: {max(registrar.values())}, true_max: {true_max}\n{registrar}')
    return 0

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )