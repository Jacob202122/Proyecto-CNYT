import math

def Modulo(a):
    p = (a[0]**2 + a[1]**2)**(1/2)
    
    return p

def Angulo(a):
    teta = math.atan2(a[1],a[0])
    return teta
    
    
def prettyPrinting(r):
    
    p = Modulo(r)
    teta = Angulo(r)
    print('(',p,',',teta,'rad )')

if __name__ == "__main__":
    
    prettyPrinting([1,1])  
