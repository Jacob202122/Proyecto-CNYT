def Conjugado(a):
    
    RealP = a[0]
    ImaginaryP = -a[1]

    return RealP, ImaginaryP

def prettyPrinting(r):

    print(r[0], '+ (', r[1],'i)')

if __name__ == '__main__':

    prettyPrinting(Conjugado([1,2]))
