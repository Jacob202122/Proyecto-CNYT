import math

def PolaresACartesianas(polar):
    
    a = polar[0]*math.cos(polar[1])
    
    b = polar[0]*math.sin(polar[1])
    
    return a, b 
    
def prettyPrinting(r):
    
    print(r[0],'+',r[1],'i')

if __name__ == "__main__":
    
    resultado = PolaresACartesianas([2**(1/2),math.pi/4])
    prettyPrinting(resultado)
