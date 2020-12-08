import sys, itertools

def main( args ):
    with open( args[1], 'r' ) as f:
        l = [ line.strip().split(' ') for line in f ]
        l = [ sorted(list( map( int, l[i] ) ),reverse=True ) for i in range( len(l) ) ]

        #part 1:
        print(sum( [ max(x) - min(x) for x in l ] ))

        #part 2:
        print( sum( [ a/b for row in l for a,b in itertools.combinations(row,2) if a%b == 0 ]))


if __name__ == '__main__':
    sys.exit( main( sys.argv ) )