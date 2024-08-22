import math

def fase(a):
    
    teta = math.atan2(a[1],a[0])
    
    return teta
    
if __name__ == "__main__":
    
    print(fase([1,1]))
