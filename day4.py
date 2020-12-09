import sys, itertools

def main( args ):
    with open( args[1], 'r' ) as f:
        l = [ sorted(line.strip().split(' ')) for line in f ]
        #print(l)
    tot = 0
    for list in l:
        wrong = 0
        for i in range(len(list)):
            if list[i] in itertools.islice(list,i+1,len(list)+1):
                #print(f'list contains duplicate. {list[i]} appears more than once in {list}')
                wrong =1
            elif sorted(list[i]) in [ sorted(e) for e in itertools.islice(list,i+1,len(list)+1) ]:
                wrong = 1
        tot += wrong
    ans = len(l) - tot
    print(ans)
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )