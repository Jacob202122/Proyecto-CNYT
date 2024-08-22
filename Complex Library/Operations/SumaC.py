def SumC(a,b):

    RealP = a[0]+b[0]
    ImaginaryP = a[1] + b[1]

    return RealP, ImaginaryP

def prettyPrinting(r):

    print(r[0],'+',r[1],'i')


if __name__ =='__main__':

    prettyPrinting(SumC([3,-1],[1,4]))
