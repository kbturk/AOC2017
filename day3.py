import sys

def solver(input):
    spot = [1, 0, 0]
    i = 1
    while spot[0] < input:
        m,n = 0,0
        #4 steps total.
        #1st step: move left.
        for m in range(i):
            spot = [spot[0]+1,spot[1]+1,spot[2]]
            if spot[0] == input:
                return spot
        #2nd step: move up.
        for n in range(i):
            spot = [spot[0]+1,spot[1],spot[2]+1]
            if spot[0] == input:
                return spot
        i += 1
        #3rd step: move right.
        for n in range(i):
            spot = [spot[0]+1,spot[1]-1,spot[2]]
            if spot[0] == input:
                return spot
        #4th step: move down.
        for n in range(i):
            spot = [spot[0]+1,spot[1],spot[2]-1]
            if spot[0] == input:
                return spot
        i += 1
    return spot

def next_coords(x,y):
    if x == y == 0: return (1,0)
    if y > -x and x > y: return (x, y+1)
    if y > -x and x <= y: return (x-1, y)
    if y <= -x and x < y: return (x, y-1)
    if y <= -x and x >= y: return (x+1, y)
    print(f'made it to the end.x:{x}, y:{y}')

def main( args ):
    input = 325489
    #part 1:
    print(abs(solver(input)[1])+abs(solver(input)[2]))
    #part 2:
    x, y = 0,0
    vals = {(0,0):1}
    while vals[(x,y)] <= input:
        (x,y) = next_coords(x,y)
        vals[(x,y)] = sum(vals.get((x+i, y+j),0) for i in [-1,0,1] for j in [-1,0,1])
    print(vals[(x,y)])
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )