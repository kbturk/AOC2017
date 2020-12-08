import sys, itertools

def main( args ):
    with open( args[1], 'r' ) as f:
        l = [ line.strip().split(' ') for line in f ]
        l = [ sorted(list( map( int, l[i] ) ),reverse=True ) for i in range( len(l) ) ]

        #part 1:
        print(sum( [ max(x) - min(x) for x in l ] ))

        #part 2:
        ans2 = []
        for row in l:
            for i in range( len( row ) - 1 ):
                for j in range(i+1,len( row )):
                    if row[i]%row[j] == 0:
                        ans2.append(row[i]/row[j])
        print(sum(ans2))

if __name__ == '__main__':
    sys.exit( main( sys.argv ) )