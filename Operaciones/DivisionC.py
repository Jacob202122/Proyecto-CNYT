def DivC(a,b):
    
    RealP = (a[0]*b[0] + a[1]*b[1])/(b[0]**2 + b[1]**2)
    ImaginaryP = (a[1]*b[0] - a[0]*b[1])/(b[0]**2 + b[1]**2)

    return RealP, ImaginaryP

def prettyPrinting(r):
    print(r[0],'+', r[1],'i')

if __name__ == "__main__":
    prettyPrinting(DivC([0,1],[1,2]))
