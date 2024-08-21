import math

def Cartesianas_a_polares(a):
    p = (a[0]**2 + a[1]**2)**(1/2)
    teta = math.atan2(a[1],a[0])
    
    return p, teta
    
def prettyPrinting(r):

    print('(',r[0],',',r[1],'rad )')

if __name__ == "__main__":
    
    prettyPrinting(Cartesianas_a_polares([1,1]))  
