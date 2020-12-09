import sys, itertools
from copy import deepcopy

def reorder_blocks(l):
    reorder_spot = l.index(max(l))
    blocks = l[reorder_spot]
    l[reorder_spot] = 0

    while blocks:
        reorder_spot += 1
        if reorder_spot > len(l)-1:
            reorder_spot = 0
        l[reorder_spot] += 1
        blocks -= 1
    return(l)

def main( args ):
    with open( args[1], 'r' ) as f:
        l = [int(c) for line in f for c in line.strip().split()]
        #print(l)

    #part1
    seen = []
    count = 0
    while l not in seen:
        seen.append(deepcopy(l))
        reorder_blocks(l)
        count += 1

    print(count, l)

    #part 2
    print(len(seen)-seen.index(l))

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )