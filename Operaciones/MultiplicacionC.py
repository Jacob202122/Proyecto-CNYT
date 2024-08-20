def MultC(a,b):

    Realp = a[0]*b[0] - a[1]*b[1]
    ImaginaryP = a[0]*b[1] + a[1]*b[0]

    return Realp, ImaginaryP

def prettyPrinting(r):

    print(r[0],'+',r[1],'i')

if __name__ == "__main__":

    prettyPrinting(MultC([3,-2],[1,2]))
