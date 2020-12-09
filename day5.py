import sys, itertools

def walking_dead(i,l, season):
    #print(f'i: {i}, l: {l}')
    if season == 2:
        if l[i] >=3:
            l[i] += -1
            i += l[i]+1
        else:
            l[i] += 1
            i += l[i]-1
        #print(f'i: {i}, l: {l}')
        return i,l
    l[i] += 1
    i += l[i]-1
        
    #print(f'i: {i},l: {l}')
    return i,l
 
def main( args ):
    with open( args[1], 'r' ) as f:
        l = [ int(line.strip()) for line in f ]
    #part 1/2:
    i,sum,season = 0,0,2
    while i <= len(l)-1:
        i,l = walking_dead(i,l,season)
        #print(f'walking..')
        sum +=1
    print(sum)

    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )